library(metafor)
library(tidylog)
library(tidyverse)
library(broom)
library(effectsize)


# Read data


# Or create random numbers

gamma_psd <- rnorm(1440)
study_sites <- as.character(rep(c("Bologna", "Würzburg", "Regensburg", "Hong Kong", "Rotterdam", "Hildesheim",
                                  "Augsburg", "Hamburg", "Potsdam"),each = 160))
phase <- as.factor(rep(c("acq","acq","ext","ext"),times = 360))
cue <- as.factor(rep(c("csp","csm"), times = 720))
ID <- as.factor(rep(1:360,each = 4))

gamma_df <- data.frame(ID,study_sites,phase,cue,gamma_psd)


# Test H1) Increased Gamma PSDs for CS+ compared to CS- pooled across all sites
# T-test 

gamma_df %>%
  filter(phase == "acq") %>%
  t.test(data = ., gamma_psd ~ cue, paired = T)

# Plot

gamma_df %>%
  filter(phase == "acq") %>%
  group_by(cue) %>%
  summarize(mean = mean(gamma_psd),
            se = sd(gamma_psd)/sqrt(n())) %>% 
  ggplot(aes(x = cue, y = mean)) + 
  geom_errorbar(aes(ymin = mean-se, ymax = mean+se), width = 0.2) + 
  geom_point(aes(fill = cue), size = 4, shape = 21) + 
  scale_y_continuous("Gamma Power") +
  scale_x_discrete("Condition", labels = c("CS-","CS+")) +
  theme_bw() +
  theme(legend.position = "none")

# Prepare Meta-Analysis

### run t-test in each lab separately

gamma_df.t <- gamma_df %>%
  filter(phase == "acq") %>%
  group_by(study_sites) %>%
  do(models = tidy(t.test(gamma_psd ~ cue, data = ., paired=T))) %>% 
  unnest(models) %>%
  select(study_sites,statistic,p.value,parameter)

# effect size per lab

gamma_df.d <- gamma_df.t %>%
  group_by(study_sites) %>%
  do(models = tidy(t_to_d(.$statistic,.$parameter,paired = T))) %>% 
  unnest(models) %>%
  select(study_sites,column, mean) %>%
  pivot_wider(.,names_from = column, values_from = mean) %>%
  mutate(SE = (CI_high-CI_low)/3.92) %>%
  select(study_sites,d,SE)

# N per lab

gamma_df.N <- gamma_df %>% 
  group_by(study_sites) %>%
  distinct(ID) %>%
  tally()

gamma_df.merged <- 
  left_join(gamma_df.t,gamma_df.d
            , by = "study_sites") %>%
  left_join(.,gamma_df.N, by = "study_sites") %>%
  select(study_sites,d,SE,n)


# extract list of the labs

labList <- gamma_df.merged$study_sites

################################################################################
### meta-analyses ##############################################################
################################################################################

meta.gamma <- rma(yi=d, sei=SE, data=gamma_df.merged, method="REML")
meta.gamma

########################################################################
###################### FOREST AND FUNNEL PLOTS #########################
########################################################################

forest(meta.gamma,slab=labList)  

funnel(meta.gamma, main='Gamma Power')

########################################################################
############################# REPORT RESULTS ###########################
########################################################################

report.meta <- function(res.meta,note) {
  # print the results
  paste(note,
        sprintf("dz = %.2f, %s, 95%% CI [%.2f, %.2f], Q(12) = %.1f, p = %.3f, I2 = %.1f %%", 
                res.meta$b,
                ifelse(res.meta$pval<0.001,'p < 0.001',paste('p =',as.character(format(res.meta$pval,digits=3)))),
                res.meta$ci.lb,
                res.meta$ci.ub,
                res.meta$QE,
                res.meta$QEp,
                res.meta$I2)
  )
}

report.meta(meta.gamma,"Gamma Power;")
