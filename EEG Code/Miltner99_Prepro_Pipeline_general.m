
%% Read Data
% read Brain Vision data
EEG = pop_loadbv('REG_Pilot1.vhdr', [], []);
EEG = pop_chanedit(EEG, 'lookup','E:\\Matlab\\eeglab2022.1\\plugins\\dipfit\\standard_BEM\\elec\\standard_1005.elc'); 

%% resample to 200 Hz
EEG = pop_resample(EEG, 200); 

%% Filter 1 Hz high pass
EEG = pop_eegfiltnew(EEG, 'locutoff',1,'plotfreqz',0);
 
%% Reref to Average Reference (keep Ref if necessary)
EEG = pop_reref( EEG, [])  
chanlocs_pre = EEG.chanlocs; %save chanlocs for later interpolation
 
%% PREP: Use the PREP Pipeline for eliminating line noise, noisy channels, and robust referencing
% Set up the params structure 
basename = EEG.setname;
params = struct();
params.lineFrequencies = [50 100]; %50 Hz line noise
params.referenceChannels = 1:EEG.nbchan; % all channels
params.evaluationChannels = 1:EEG.nbchan;
params.rereferencedChannels = 1:EEG.nbchan;
params.detrendChannels = 1:EEG.nbchan;
params.lineNoiseChannels = 1:EEG.nbchan;
params.ignoreBoundaryEvents = true;
params.detrendType = 'high pass';
params.detrendCutoff = 1;
params.referenceType = 'robust';
params.meanEstimateType = 'median';
params.interpolationOrder = 'post-reference';
params.removeInterpolatedChannels = true;
params.keepFiltered = false;
basenameOut = [basename 'robust_1Hz_post_median_unfiltered'];
params.name = EEG.setname;

% Run PREP
[EEG, params, computationTimes] = prepPipeline(EEG, params);

% Print PREP Computation Time
fprintf('Computation times (seconds):\n   %s\n', ...
        getStructureString(computationTimes));
    
%% Remove bad channels
EEG = pop_select(EEG, 'nochannel', EEG.etc.noiseDetection.interpolatedChannelNumbers);

%% segmentation (cue-related -250ms:3000ms) & baseline-correction (-250ms:0ms pre cue)
EEG = pop_epoch( EEG, {'S  1' 'S  2' 'S  3' 'S  4'}, [-0.25 3], 'epochinfo', 'yes');

%Read Trigger-File to replace system-specific trigger labels with uniform labels
triggerFile = importdata('REG_Pilot1_Trigger.dat');

for i = 1:length(EEG.event)
    EEG.event(i).type = triggerFile(i); 
end

%% Run ICA
EEG = pop_runica(EEG, 'extended',1,'interupt','on');

%% Compute bad components using MARA with default parameters
[artcomps, info] = MARA(EEG);
EEG.reject.MARAinfo = info;

%% Reject componens
EEG.reject.gcompreject(artcomps) = 1; 
EEG  = pop_subcomp(EEG,[],0);

%% Interpolation of bad channels
EEG = pop_interp(EEG,chanlocs_pre)

%% Reject remaining bad segments (epochs deviating more than 3.29 SD (Ref Tabachnik 2007) from trimmed normalized means with respect to joint probability, kurtosis or the spectrum.
CleanEpochs = ones(1,EEG.trials);
threshold_DB = 90;
threshold_SD = 3.29;

% Check Frequency Spectrum
[~, badSpectrum] = pop_rejspec(EEG, 1, 'elecrange', [1:EEG.nbchan], 'threshold', [-threshold_DB threshold_DB], 'freqlimits', [1 49]);
CleanEpochs(badSpectrum) = 0;

% Check Kurtosis
badKurtosis = pop_rejkurt(EEG, 1, [1:EEG.nbchan],  threshold_SD,threshold_SD,0,0,0);
badKurtosis = find(badKurtosis.reject.rejkurt);
CleanEpochs(badKurtosis) = 0;

% Check Probability 
badProbability = pop_jointprob(EEG, 1, [1:EEG.nbchan],  threshold_SD, threshold_SD,0,0,0);
badProbability = find(badProbability.reject.rejjp);
CleanEpochs(badProbability) = 0;

% Save good epochs in datafile
goodTrials = dataset({CleanEpochs','trial_number'});
export(goodTrials,'file','Reg1_goodTrials.csv','Delimiter',';') % Change name and directory 

% Remove bad Epochs
EEG = pop_select( EEG, 'trial',find(CleanEpochs));


%% CSD transformation with fixed parameters
EEG = pop_currentsourcedensity(EEG);
%EEG = pop_currentsourcedensity_stegmann(EEG);

%% Save/Load preprocessed data
%EEG = pop_saveset( EEG, 'filename', 'Reg1_processed','filepath',write_dir);
%EEG = pop_loadset( strcat(write_dir,'Reg1_processed.set'));

%% Kalman filter  

% Define parameters
baselineWindow = 20:50; % baseline in samplepoints (200 Hz) = 0.1 - 0.25 s prior to cue onset
p = 16; % model order
freqs = (1:45)'; % FOIs
fs = 200; %samplerate
electrodes = ["Oz", 'O1', 'O2', 'Pz', ... %Oz, O1, O2, Pz, 
    'CPz', 'CP1', 'CP2', 'CP3', 'CP4', ... %CPz, CP1, CP2, CP3, CP4
    'Cz', 'C1', 'C2' 'C3', 'C4', ... %Cz, C1, C2, C3, C4
    'FCz', 'FC1', 'FC2', 'FC3', 'FC4'];  ... %FCz, FC1, FC2, FC3, FC4

chanIndex = zeros(1,length(electrodes));

for sensor = 1:length(electrodes)
    chanIndex(sensor) = find(strcmp({EEG.chanlocs.labels},...
        electrodes{sensor}));
end

%% keep only CS+ trials in Acq

% Rearrange EEG data structure
EEG_AcqCSp = pop_epoch( EEG, {  '1'  }, [-0.25 3], 'epochinfo', 'yes');
dataAcqCSp = permute(EEG_AcqCSp.data, [3,1,2]);
dataAcqCSp = dataAcqCSp(:,chanIndex,:);

% Run Kalman-Filter AR
KF = dynet_SSM_KF(dataAcqCSp,p,0.03); %order = 16, adaptation constant = 0.03

[nodes,~,~,time] = size(KF.AR);

Z = exp(-2*pi*1i*freqs/fs).^(1:p);
H_complex        = repmat(eye(nodes), [1 1 length(freqs) time]);
for k = 1:p
    tmp  = repmat(-KF.AR(:, :, k,:), [1 1 length(freqs) 1]);
    H_complex    = H_complex + bsxfun(@times,tmp,reshape(Z(:,k),1,1,[]));
end

 S = NaN(nodes,nodes,numel(freqs),time);
 R = median(KF.R(:,:,round(time/2):end),3);

for t = 1:time
    for f = 1:numel(freqs)
        H_ft        = squeeze(H_complex(:,:,f,t));
        S(:,:,f,t) =H_ft\KF.R(:,:,t)/H_ft'; %oder s. oben nur R
    end
end
    
% now calculate coherence values, see eq (29 in Arnolds)
coherenceAcqCSp = zeros(nodes,nodes,numel(freqs),time);    
for t = p+1:time %cycle through time
    for f = 1:numel(freqs) %cycle through freqs
        for s1 = 1:nodes %cycle through
            for s2= 1:nodes %pairs of eeg sensors
               coherenceAcqCSp(s1,s2,f,t) = abs(S(s1,s2,f,t))./sqrt(real(S(s1,s1,f,t).*S(s2,s2,f,t)));
               if s1 == s2
                    coherenceAcqCSp(s1,s2,f,t)  = abs(S(s1,s2,f,t));
               end
            end
        end
    end
end   

% Baseline-correct PSD values for diagonals (change in %)
for s1 = 1:nodes %cycle through diagonal
    for f = 1:numel(freqs) %cycle through freqs
        coherenceAcqCSp(s1,s1,f,:)  = (coherenceAcqCSp(s1,s2,f,:)-mean(coherenceAcqCSp(s1,s2,f,baselineWindow)))./mean(coherenceAcqCSp(s1,s2,f,baselineWindow)).*100;
   end
end
          
%% now the same for CS- trials in Acq

EEG_AcqCSm = pop_epoch( EEG, {  '2'  }, [-0.25 3], 'epochinfo', 'yes');
dataAcqCSm = permute(EEG_AcqCSm.data, [3,1,2]);
dataAcqCSm = dataAcqCSm(:,chanIndex,:);

KF = dynet_SSM_KF(dataAcqCSm,p,0.03); %order = 16, adaptation constant = 0.03

[nodes,~,~,time] = size(KF.AR);

Z = exp(-2*pi*1i*freqs/fs).^(1:p);
H_complex        = repmat(eye(nodes), [1 1 length(freqs) time]);
for k = 1:p
    tmp  = repmat(-KF.AR(:, :, k,:), [1 1 length(freqs) 1]);
    H_complex    = H_complex + bsxfun(@times,tmp,reshape(Z(:,k),1,1,[]));
end

S = NaN(nodes,nodes,numel(freqs),time);
R = median(KF.R(:,:,round(time/2):end),3);

for t = 1:time
    for f = 1:numel(freqs)
        H_ft        = squeeze(H_complex(:,:,f,t));
        S(:,:,f,t) =H_ft\KF.R(:,:,t)/H_ft'; %oder s. oben nur R
    end
end

% now calculate coherence values, see eq (29 in Arnolds)
coherenceAcqCSm = zeros(nodes,nodes,numel(freqs),time);    
for t = p+1:time %cycle through time
    for f = 1:numel(freqs) %cycle through freqs
        for s1 = 1:nodes %cycle through
            for s2= 1:nodes %pairs of eeg sensors
               coherenceAcqCSm(s1,s2,f,t) = abs(S(s1,s2,f,t))./sqrt(real(S(s1,s1,f,t).*S(s2,s2,f,t)));
               if s1 == s2
                    coherenceAcqCSm(s1,s2,f,t)  = abs(S(s1,s2,f,t));
               end
            end
        end
    end
end

for s1 = 1:nodes %cycle through diagonal
    for f = 1:numel(freqs) %cycle through freqs
        coherenceAcqCSm(s1,s1,f,:)  = (coherenceAcqCSm(s1,s2,f,:)-mean(coherenceAcqCSm(s1,s2,f,baselineWindow)))./mean(coherenceAcqCSm(s1,s2,f,baselineWindow)).*100;
   end
end
        
%% now the same for CS+ trials in Ext

EEG_ExtCSp = pop_epoch( EEG, {  '3'  }, [-0.25 3], 'epochinfo', 'yes');
dataExtCSp = permute(EEG_ExtCSp.data, [3,1,2]);
dataExtCSp = dataExtCSp(:,chanIndex,:);

KF = dynet_SSM_KF(dataExtCSp,p,0.03); %order = 16, adaptation constant = 0.03

[nodes,~,~,time] = size(KF.AR);

Z = exp(-2*pi*1i*freqs/fs).^(1:p);
H_complex        = repmat(eye(nodes), [1 1 length(freqs) time]);
for k = 1:p
    tmp  = repmat(-KF.AR(:, :, k,:), [1 1 length(freqs) 1]);
    H_complex    = H_complex + bsxfun(@times,tmp,reshape(Z(:,k),1,1,[]));
end

S = NaN(nodes,nodes,numel(freqs),time);
R = median(KF.R(:,:,round(time/2):end),3);

for t = 1:time
    for f = 1:numel(freqs)
        H_ft        = squeeze(H_complex(:,:,f,t));
        S(:,:,f,t) =H_ft\KF.R(:,:,t)/H_ft'; %oder s. oben nur R
    end
end

% now calculate coherence values, see eq (29 in Arnolds)
coherenceExtCSp = zeros(nodes,nodes,numel(freqs),time);    
for t = p+1:time %cycle through time
    for f = 1:numel(freqs) %cycle through freqs
        for s1 = 1:nodes %cycle through
            for s2= 1:nodes %pairs of eeg sensors
               coherenceExtCSp(s1,s2,f,t) = abs(S(s1,s2,f,t))./sqrt(real(S(s1,s1,f,t).*S(s2,s2,f,t)));
               if s1 == s2
                    coherenceExtCSp(s1,s2,f,t)  = abs(S(s1,s2,f,t));
               end
            end
        end
    end
end

for s1 = 1:nodes %cycle through diagonal
    for f = 1:numel(freqs) %cycle through freqs
        coherenceExtCSp(s1,s1,f,:)  = (coherenceExtCSp(s1,s2,f,:)-mean(coherenceExtCSp(s1,s2,f,baselineWindow)))./mean(coherenceExtCSp(s1,s2,f,baselineWindow)).*100;
   end
end
  
        
%% keep only CS- in Acq

EEG_ExtCSm = pop_epoch( EEG, {  '4'  }, [-0.25 3], 'epochinfo', 'yes');
dataExtCSm = permute(EEG_ExtCSm.data, [3,1,2]);
dataExtCSm = dataExtCSm(:,chanIndex,:);

KF = dynet_SSM_KF(dataExtCSm,p,0.03); %order = 16, adaptation constant = 0.03

[nodes,~,~,time] = size(KF.AR);

Z = exp(-2*pi*1i*freqs/fs).^(1:p);
H_complex        = repmat(eye(nodes), [1 1 length(freqs) time]);
for k = 1:p
    tmp  = repmat(-KF.AR(:, :, k,:), [1 1 length(freqs) 1]);
    H_complex    = H_complex + bsxfun(@times,tmp,reshape(Z(:,k),1,1,[]));
end

S = NaN(nodes,nodes,numel(freqs),time);
R = median(KF.R(:,:,round(time/2):end),3);


for t = 1:time
    for f = 1:numel(freqs)
        H_ft        = squeeze(H_complex(:,:,f,t));
        S(:,:,f,t) =H_ft\KF.R(:,:,t)/H_ft'; %oder s. oben nur R
    end
end

% now calculate coherence values, see eq (29 in Arnolds)
coherenceExtCSm = zeros(nodes,nodes,numel(freqs),time);    
for t = p+1:time %cycle through time
    for f = 1:numel(freqs) %cycle through freqs
        for s1 = 1:nodes %cycle through
            for s2= 1:nodes %pairs of eeg sensors
               coherenceExtCSm(s1,s2,f,t) = abs(S(s1,s2,f,t))./sqrt(real(S(s1,s1,f,t).*S(s2,s2,f,t)));
               if s1 == s2
                    coherenceExtCSm(s1,s2,f,t)  = abs(S(s1,s2,f,t));
               end
            end
        end
    end
end

for s1 = 1:nodes %cycle through diagonal
    for f = 1:numel(freqs) %cycle through freqs
        coherenceExtCSm(s1,s1,f,:)  = (coherenceExtCSm(s1,s2,f,:)-mean(coherenceExtCSm(s1,s2,f,baselineWindow)))./mean(coherenceExtCSm(s1,s2,f,baselineWindow)).*100;
   end
end
         
 %% PSD Analysis
 % Reduce Dimensions and Combine Conditions to Export to Statistic Program
 
 alpha_psd = zeros(19,4); %19 sensors, 4 conditions
 foiA = 8:12; %8-12 Hz 
 toiA = 151:310; %500 - 1300 ms
 
 for s1 = 1:length(electrodes)
     co1 = coherenceAcqCSp(s1,s1,foiA,toiA); 
     co2 = coherenceAcqCSm(s1,s1,foiA,toiA); 
     co3 = coherenceExtCSp(s1,s1,foiA,toiA); 
     co4 = coherenceExtCSm(s1,s1,foiA,toiA);
     
     alpha_psd(s1,1) = mean(co1(:));
     alpha_psd(s1,2) = mean(co2(:));
     alpha_psd(s1,3) = mean(co3(:));
     alpha_psd(s1,4) = mean(co4(:));
 end
 
 gamma_psd = zeros(19,4); %19 sensors, 4 conditions
 foiG = 37:43; %37-43 Hz 
 toiG = 451:650; %2000 - 3000 ms
 
 for s1 = 1:length(electrodes)
     co1 = coherenceAcqCSp(s1,s1,foiG,toiG); 
     co2 = coherenceAcqCSm(s1,s1,foiG,toiG); 
     co3 = coherenceExtCSp(s1,s1,foiG,toiG); 
     co4 = coherenceExtCSm(s1,s1,foiG,toiG);

     gamma_psd(s1,1) = mean(co1(:));
     gamma_psd(s1,2) = mean(co2(:));
     gamma_psd(s1,3) = mean(co3(:));
     gamma_psd(s1,4) = mean(co4(:));
 end 
 
%% Coherence Analysis
 foiG = 37:43; %37-43 Hz 
 toiG = 601:650; %2750 - 3000 ms
 
  for s1 = 1:length(electrodes)
      for s2 = 1:length(electrodes)
         co1 = atanh(coherenceAcqCSp(s1,s2,foiG,toiG)); 
         co2 = atanh(coherenceAcqCSm(s1,s2,foiG,toiG)); 
         co3 = atanh(coherenceExtCSp(s1,s2,foiG,toiG)); 
         co4 = atanh(coherenceExtCSm(s1,s2,foiG,toiG));

        gamma_z(s1,s2,1) = mean(mean(co1,4),3);
        gamma_z(s1,s2,2) = mean(mean(co2,4),3);
        gamma_z(s1,s2,3) = mean(mean(co3,4),3);
        gamma_z(s1,s2,4) = mean(mean(co4,4),3);
     end
 end 
 
 