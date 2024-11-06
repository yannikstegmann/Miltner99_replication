#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.4),
    on Juli 16, 2024, at 16:05
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.1.4'
expName = 'Miltner1999_Threshold'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': '',
    'USPort': '0xD010',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [2560, 1440]
_loggingLevel = logging.getLevel('exp')
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # override logging level
    _loggingLevel = logging.getLevel(
        prefs.piloting['pilotLoggingLevel']
    )

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='E:\\PsychoPy Miltner\\Deutsch\\Miltner1999 - Pain Threshold_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(_loggingLevel)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=_loggingLevel)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=1,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.mouseVisible = False
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('instr_resp') is None:
        # initialise instr_resp
        instr_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='instr_resp',
        )
    if deviceManager.getDevice('pain_resp') is None:
        # initialise pain_resp
        pain_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='pain_resp',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "instr_1" ---
    Instr_text = visual.TextStim(win=win, name='Instr_text',
        text='Willkommen und vielen Dank für Ihre Teilnahme an diesem Experiment. \nWir werden nun die Intensität der elektrischen Reize kalibrieren.\n\nSie werden eine Reihe von Reizen erleben.\nBitte geben Sie für jede Empfindung an, wie schmerzhaft Sie diese empfinden. Verwenden Sie dabei die folgende Skala:\n\n\n--- Drücken Sie die Leertaste um fortzufahren ---',
        font='Arial',
        pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    instr_resp = keyboard.Keyboard(deviceName='instr_resp')
    # Run 'Begin Experiment' code from trigger_and_mouse_code
    import time
    
    
    from psychopy import parallel
    parallel.setPortAddress(expInfo['USPort']) # EEGPort 0x0378 or 0xC010 
    def sendTrigger(triggerCode):
        if isinstance(triggerCode, np.integer):
            triggerCode = triggerCode.item()
        parallel.setData(triggerCode)
        time.sleep(0.002) #wait 2 ms
        parallel.setData(0) # set Trigger Channel back to 0
        time.sleep(0.002) #wait 2 ms
        parallel.setData(triggerCode)
        time.sleep(0.002) #wait 2 ms
        parallel.setData(0) # set Trigger Channel back to 0
        time.sleep(0.002) #wait 2 ms
        parallel.setData(triggerCode)
        time.sleep(0.002) #wait 2 ms
        parallel.setData(0) # set Trigger Channel back to 0
    
    
    # --- Initialize components for Routine "iti" ---
    iti_text = visual.TextStim(win=win, name='iti_text',
        text='',
        font='Arial',
        pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "us" ---
    us_text = visual.TextStim(win=win, name='us_text',
        text='+',
        font='Arial',
        pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
        color=[1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "pain_scale" ---
    pain_slider = visual.Slider(win=win, name='pain_slider',
        startValue=None, size=(1.0, 0.05), pos=(0, -0.1), units=win.units,
        labels=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), ticks=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=0.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=0, readOnly=False)
    pain_resp = keyboard.Keyboard(deviceName='pain_resp')
    us_anchor_min = visual.TextStim(win=win, name='us_anchor_min',
        text='gar nicht \nschmerzhaft',
        font='Arial',
        pos=(-0.5, -0.3), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    us_anchor_max = visual.TextStim(win=win, name='us_anchor_max',
        text='unerträglich\nschmerzhaft',
        font='Arial',
        pos=(0.5, -0.3), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "instr_1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instr_1.started', globalClock.getTime(format='float'))
    instr_resp.keys = []
    instr_resp.rt = []
    _instr_resp_allKeys = []
    # Run 'Begin Routine' code from trigger_and_mouse_code
    win.mouseVisible = False
    
    # keep track of which components have finished
    instr_1Components = [Instr_text, instr_resp]
    for thisComponent in instr_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instr_1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Instr_text* updates
        
        # if Instr_text is starting this frame...
        if Instr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instr_text.frameNStart = frameN  # exact frame index
            Instr_text.tStart = t  # local t and not account for scr refresh
            Instr_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instr_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instr_text.started')
            # update status
            Instr_text.status = STARTED
            Instr_text.setAutoDraw(True)
        
        # if Instr_text is active this frame...
        if Instr_text.status == STARTED:
            # update params
            pass
        
        # *instr_resp* updates
        waitOnFlip = False
        
        # if instr_resp is starting this frame...
        if instr_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_resp.frameNStart = frameN  # exact frame index
            instr_resp.tStart = t  # local t and not account for scr refresh
            instr_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instr_resp.started')
            # update status
            instr_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instr_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instr_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instr_resp.status == STARTED and not waitOnFlip:
            theseKeys = instr_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _instr_resp_allKeys.extend(theseKeys)
            if len(_instr_resp_allKeys):
                instr_resp.keys = _instr_resp_allKeys[-1].name  # just the last key pressed
                instr_resp.rt = _instr_resp_allKeys[-1].rt
                instr_resp.duration = _instr_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instr_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instr_1" ---
    for thisComponent in instr_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instr_1.stopped', globalClock.getTime(format='float'))
    # check responses
    if instr_resp.keys in ['', [], None]:  # No response was made
        instr_resp.keys = None
    thisExp.addData('instr_resp.keys',instr_resp.keys)
    if instr_resp.keys != None:  # we had a response
        thisExp.addData('instr_resp.rt', instr_resp.rt)
        thisExp.addData('instr_resp.duration', instr_resp.duration)
    thisExp.nextEntry()
    # the Routine "instr_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "iti" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('iti.started', globalClock.getTime(format='float'))
    iti_text.setText('+')
    # keep track of which components have finished
    itiComponents = [iti_text]
    for thisComponent in itiComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "iti" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *iti_text* updates
        
        # if iti_text is starting this frame...
        if iti_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            iti_text.frameNStart = frameN  # exact frame index
            iti_text.tStart = t  # local t and not account for scr refresh
            iti_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(iti_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'iti_text.started')
            # update status
            iti_text.status = STARTED
            iti_text.setAutoDraw(True)
        
        # if iti_text is active this frame...
        if iti_text.status == STARTED:
            # update params
            pass
        
        # if iti_text is stopping this frame...
        if iti_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > iti_text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                iti_text.tStop = t  # not accounting for scr refresh
                iti_text.tStopRefresh = tThisFlipGlobal  # on global time
                iti_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'iti_text.stopped')
                # update status
                iti_text.status = FINISHED
                iti_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in itiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "iti" ---
    for thisComponent in itiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('iti.stopped', globalClock.getTime(format='float'))
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    forever = data.TrialHandler(nReps=1000, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='forever')
    thisExp.addLoop(forever)  # add the loop to the experiment
    thisForever = forever.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisForever.rgb)
    if thisForever != None:
        for paramName in thisForever:
            globals()[paramName] = thisForever[paramName]
    
    for thisForever in forever:
        currentLoop = forever
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisForever.rgb)
        if thisForever != None:
            for paramName in thisForever:
                globals()[paramName] = thisForever[paramName]
        
        # --- Prepare to start Routine "us" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('us.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from us_code
        sendTrigger(128)
        # keep track of which components have finished
        usComponents = [us_text]
        for thisComponent in usComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "us" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.3:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *us_text* updates
            
            # if us_text is starting this frame...
            if us_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                us_text.frameNStart = frameN  # exact frame index
                us_text.tStart = t  # local t and not account for scr refresh
                us_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(us_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'us_text.started')
                # update status
                us_text.status = STARTED
                us_text.setAutoDraw(True)
            
            # if us_text is active this frame...
            if us_text.status == STARTED:
                # update params
                pass
            
            # if us_text is stopping this frame...
            if us_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > us_text.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    us_text.tStop = t  # not accounting for scr refresh
                    us_text.tStopRefresh = tThisFlipGlobal  # on global time
                    us_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'us_text.stopped')
                    # update status
                    us_text.status = FINISHED
                    us_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in usComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "us" ---
        for thisComponent in usComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('us.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.300000)
        
        # --- Prepare to start Routine "pain_scale" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('pain_scale.started', globalClock.getTime(format='float'))
        pain_slider.reset()
        pain_resp.keys = []
        pain_resp.rt = []
        _pain_resp_allKeys = []
        # keep track of which components have finished
        pain_scaleComponents = [pain_slider, pain_resp, us_anchor_min, us_anchor_max]
        for thisComponent in pain_scaleComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "pain_scale" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *pain_slider* updates
            
            # if pain_slider is starting this frame...
            if pain_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                pain_slider.frameNStart = frameN  # exact frame index
                pain_slider.tStart = t  # local t and not account for scr refresh
                pain_slider.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pain_slider, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pain_slider.started')
                # update status
                pain_slider.status = STARTED
                pain_slider.setAutoDraw(True)
            
            # if pain_slider is active this frame...
            if pain_slider.status == STARTED:
                # update params
                pass
            
            # *pain_resp* updates
            waitOnFlip = False
            
            # if pain_resp is starting this frame...
            if pain_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                pain_resp.frameNStart = frameN  # exact frame index
                pain_resp.tStart = t  # local t and not account for scr refresh
                pain_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pain_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pain_resp.started')
                # update status
                pain_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(pain_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(pain_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if pain_resp.status == STARTED and not waitOnFlip:
                theseKeys = pain_resp.getKeys(keyList=['s'], ignoreKeys=["escape"], waitRelease=False)
                _pain_resp_allKeys.extend(theseKeys)
                if len(_pain_resp_allKeys):
                    pain_resp.keys = _pain_resp_allKeys[-1].name  # just the last key pressed
                    pain_resp.rt = _pain_resp_allKeys[-1].rt
                    pain_resp.duration = _pain_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *us_anchor_min* updates
            
            # if us_anchor_min is starting this frame...
            if us_anchor_min.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                us_anchor_min.frameNStart = frameN  # exact frame index
                us_anchor_min.tStart = t  # local t and not account for scr refresh
                us_anchor_min.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(us_anchor_min, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'us_anchor_min.started')
                # update status
                us_anchor_min.status = STARTED
                us_anchor_min.setAutoDraw(True)
            
            # if us_anchor_min is active this frame...
            if us_anchor_min.status == STARTED:
                # update params
                pass
            
            # *us_anchor_max* updates
            
            # if us_anchor_max is starting this frame...
            if us_anchor_max.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                us_anchor_max.frameNStart = frameN  # exact frame index
                us_anchor_max.tStart = t  # local t and not account for scr refresh
                us_anchor_max.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(us_anchor_max, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'us_anchor_max.started')
                # update status
                us_anchor_max.status = STARTED
                us_anchor_max.setAutoDraw(True)
            
            # if us_anchor_max is active this frame...
            if us_anchor_max.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pain_scaleComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "pain_scale" ---
        for thisComponent in pain_scaleComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('pain_scale.stopped', globalClock.getTime(format='float'))
        forever.addData('pain_slider.response', pain_slider.getRating())
        forever.addData('pain_slider.rt', pain_slider.getRT())
        # check responses
        if pain_resp.keys in ['', [], None]:  # No response was made
            pain_resp.keys = None
        forever.addData('pain_resp.keys',pain_resp.keys)
        if pain_resp.keys != None:  # we had a response
            forever.addData('pain_resp.rt', pain_resp.rt)
            forever.addData('pain_resp.duration', pain_resp.duration)
        # the Routine "pain_scale" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1000 repeats of 'forever'
    
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
