#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.5),
    on November 05, 2024, at 11:53
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
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware, parallel
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
psychopyVersion = '2024.1.5'
expName = 'Miltner1999'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': '',
    'order': '1',
    'EEGPort': '0x0378',
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
        originPath='E:\\Experimente\\Experiment - EEGManylabs - Miltner1999\\PsychoPy Miltner\\Deutsch\\Miltner1999_lastrun.py',
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
            monitor='EEGMonitor', color=[0,0,0], colorSpace='rgb',
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
    win.mouseVisible = True
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
    if deviceManager.getDevice('instr_2_resp') is None:
        # initialise instr_2_resp
        instr_2_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='instr_2_resp',
        )
    if deviceManager.getDevice('instr_3_resp') is None:
        # initialise instr_3_resp
        instr_3_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='instr_3_resp',
        )
    if deviceManager.getDevice('instr_e_resp') is None:
        # initialise instr_e_resp
        instr_e_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='instr_e_resp',
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
        text='Herzlich willkommen und vielen Dank für die Teilnahme an diesem Experiment.\n\n\n--- Drücken Sie die Leertaste um fortzufahren ---',
        font='Arial',
        pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    instr_resp = keyboard.Keyboard(deviceName='instr_resp')
    # Run 'Begin Experiment' code from mouse_and_trigger_code
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
    
    
    # --- Initialize components for Routine "instr_2" ---
    instr_2_text = visual.TextStim(win=win, name='instr_2_text',
        text='In den nächsten 30 Minuten werden Sie verschiedene Symbole betrachten.\nIhre Aufgabe ist es dabei, sich auf das Kreuz in der Bildschirmmitte zu konzentrieren.\n\n---  Drücken Sie die Leertaste um fortzufahren  ---',
        font='Arial',
        pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    instr_2_resp = keyboard.Keyboard(deviceName='instr_2_resp')
    
    # --- Initialize components for Routine "instr_3" ---
    instr_3_text = visual.TextStim(win=win, name='instr_3_text',
        text='Zwischendurch sollen Sie regelmäßig angeben, welche Emotionen diese Stimuli in Ihnen auslösen.\nEs gibt dabei keine „richtigen“ oder „falschen“ Antworten, antworten Sie deshalb bitte so ehrlich wie möglich!\n\n---  Drücken Sie die Leertaste um fortzufahren  ---',
        font='Arial',
        pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    instr_3_resp = keyboard.Keyboard(deviceName='instr_3_resp')
    
    # --- Initialize components for Routine "practice_rating" ---
    practice_text = visual.TextStim(win=win, name='practice_text',
        text='Die Skala reicht von negativ bis positiv.\nBeim ersten Extremwert wirken die Stimuli sehr negativ auf Sie, beim anderen sehr positiv.\nWenn die Stimuli keine Wirkung auf Sie haben, also weder positiv noch negativ, \nbewegen Sie das Dreieck bitte in der Mitte.\n\nNutzen Sie die Pfeiltasten, um den blauen Marker auf dem entsprechenden Wert zu platzieren.\nDrücken Sie Enter um ihre Auswahl zu bestätigen und um mit dem Experiment fortzufahren.',
        font='Arial',
        pos=(0, 0.1), height=0.04, wrapWidth=1.1, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    practice_slider = visual.RatingScale(win=win, name='practice_slider', marker='triangle', size=1.0, pos=[0.0, -0.65], low=-4, high=4, labels=['sehr negativ', ' neutral', ' sehr positiv'], scale='Wie negativ/positiv wirkt dieser Stimulus auf Sie?', markerStart='0', showAccept=False)
    
    # --- Initialize components for Routine "practice_prating_int" ---
    pain_text_practice = visual.TextStim(win=win, name='pain_text_practice',
        text='Außerdem sollen Sie die elektrischen Reizebewerten, die Ihnen während des Experiments präsentiert werden. \n\nAuf der ersten Skala bewerten Sie, wie schmerzhaft/intensiv Sie die elektrischen Reize wahrgenommen haben. Die Skala reicht von "gar nicht schmerzhaft" bis "unerträglich schmerzhaft".\n\nNutzen Sie die Pfeiltasten, um den blauen Marker auf dem entsprechenden Wert zu platzieren.\nDrücken Sie Enter um ihre Auswahl zu bestätigen und um mit dem Experiment fortzufahren.',
        font='Arial',
        pos=(0, 0.075), height=0.035, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    practice_pain_slider = visual.RatingScale(win=win, name='practice_pain_slider', marker='triangle', size=1.0, pos=[0.0, -0.65], low=0, high=10, labels=['gar nicht schmerzhaft', ' unerträglich schmerzhaft'], scale='Wie schmerzhaft/intensiv haben Sie den letzten elektrischen Reiz wahrgenommen?', markerStart='0', showAccept=False)
    
    # --- Initialize components for Routine "practice_prating_unpl" ---
    pain_text_practice_2 = visual.TextStim(win=win, name='pain_text_practice_2',
        text='Auf der zweiten Skala sollen sie darüberhinaus bewerten wie unangenehm/störend Sie die elektrischen Reize wahrgenommen haben. Diese Skala reicht von "gar nicht unangenehm bis "sehr unangenehm".\n\nNutzen Sie die Pfeiltasten, um den blauen Marker auf dem entsprechenden Wert zu platzieren.\nDrücken Sie Enter um ihre Auswahl zu bestätigen und um mit dem Experiment fortzufahren.',
        font='Arial',
        pos=(0, 0.075), height=0.035, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    practice_pain_slider_2 = visual.RatingScale(win=win, name='practice_pain_slider_2', marker='triangle', size=1.0, pos=[0.0, -0.65], low=0, high=10, labels=['gar nicht unangenehm', ' sehr unangenehm'], scale='Wie unangenehm/störend haben Sie den letzten elektrischen Reiz wahrgenommen?', markerStart='0', showAccept=False)
    
    # --- Initialize components for Routine "instr_experimentator" ---
    instr_e_text = visual.TextStim(win=win, name='instr_e_text',
        text='Ihre Versuchsleitung wird jetzt die Aufzeichnung starten.\nHaben Sie noch Fragen?\n\n---  Bitte geben Sie jetzt Ihrer Versuchsleitung Bescheid  ---\n',
        font='Arial',
        pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    instr_e_resp = keyboard.Keyboard(deviceName='instr_e_resp')
    
    # --- Initialize components for Routine "iti" ---
    iti_text = visual.TextStim(win=win, name='iti_text',
        text='',
        font='Arial',
        pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "stim_acq" ---
    # Run 'Begin Experiment' code from marker_code_acq
    trial_i = 1
    stim = visual.Rect(
        win=win, name='stim',units='deg', 
        width=(8, 8)[0], height=(8, 8)[1],
        ori=1.0, pos=(0, 0), anchor='center',
        lineWidth=1,     colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=[-1.000,-1.000,-1.000],
        opacity=1, depth=-1.0, interpolate=True)
    p_port = parallel.ParallelPort(address='0x0378')
    
    # --- Initialize components for Routine "us" ---
    
    # --- Initialize components for Routine "short_iti" ---
    short_iti_text = visual.TextStim(win=win, name='short_iti_text',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "ratings" ---
    rating_polygon = visual.Rect(
        win=win, name='rating_polygon',
        width=(0.33, 0.33)[0], height=(0.33, 0.33)[1],
        ori=1.0, pos=(0, 0.1), anchor='center',
        lineWidth=1,     colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=[-1.000,-1.000,-1.000],
        opacity=1, depth=0.0, interpolate=True)
    cs_rating = visual.RatingScale(win=win, name='cs_rating', marker='triangle', size=1.0, pos=[0.0, -0.65], low=-4, high=4, labels=['very negative', ' neutral', ' very positive'], scale='How negative/positive do you feel while seeing this stimulus?', markerStart='0', showAccept=False)
    
    # --- Initialize components for Routine "pain_ratining_intensity" ---
    p_rating_1 = visual.RatingScale(win=win, name='p_rating_1', marker='triangle', size=1.0, pos=[0.0, -0.4], low=0, high=10, labels=['gar nicht schmerzhaft', ' unerträglich schmerzhaft'], scale='Wie schmerzhaft/intensiv haben Sie den letzten elektrischen Reiz wahrgenommen?', markerStart=0.0, showAccept=False)
    
    # --- Initialize components for Routine "paint_ratining_unpleasant" ---
    p_rating_2 = visual.RatingScale(win=win, name='p_rating_2', marker='triangle', size=1.0, pos=[0.0, -0.4], low=0, high=10, labels=['gar nicht unangenehm', ' sehr unangenehm'], scale='Wie unangenehm/störend haben Sie den letzten elektrischen Reiz wahrgenommen?', markerStart=0.0, showAccept=False)
    
    # --- Initialize components for Routine "iti" ---
    iti_text = visual.TextStim(win=win, name='iti_text',
        text='',
        font='Arial',
        pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "stim_ext" ---
    stim_2 = visual.Rect(
        win=win, name='stim_2',units='deg', 
        width=(8, 8)[0], height=(8, 8)[1],
        ori=1.0, pos=(0, 0), anchor='center',
        lineWidth=1,     colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=[-1.000,-1.000,-1.000],
        opacity=1, depth=-1.0, interpolate=True)
    p_port_2 = parallel.ParallelPort(address='0x0378')
    
    # --- Initialize components for Routine "short_iti" ---
    short_iti_text = visual.TextStim(win=win, name='short_iti_text',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "ratings" ---
    rating_polygon = visual.Rect(
        win=win, name='rating_polygon',
        width=(0.33, 0.33)[0], height=(0.33, 0.33)[1],
        ori=1.0, pos=(0, 0.1), anchor='center',
        lineWidth=1,     colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=[-1.000,-1.000,-1.000],
        opacity=1, depth=0.0, interpolate=True)
    cs_rating = visual.RatingScale(win=win, name='cs_rating', marker='triangle', size=1.0, pos=[0.0, -0.65], low=-4, high=4, labels=['very negative', ' neutral', ' very positive'], scale='How negative/positive do you feel while seeing this stimulus?', markerStart='0', showAccept=False)
    
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
    # create starting attributes for instr_resp
    instr_resp.keys = []
    instr_resp.rt = []
    _instr_resp_allKeys = []
    # Run 'Begin Routine' code from mouse_and_trigger_code
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
    
    # --- Prepare to start Routine "instr_2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instr_2.started', globalClock.getTime(format='float'))
    # create starting attributes for instr_2_resp
    instr_2_resp.keys = []
    instr_2_resp.rt = []
    _instr_2_resp_allKeys = []
    # keep track of which components have finished
    instr_2Components = [instr_2_text, instr_2_resp]
    for thisComponent in instr_2Components:
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
    
    # --- Run Routine "instr_2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_2_text* updates
        
        # if instr_2_text is starting this frame...
        if instr_2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_2_text.frameNStart = frameN  # exact frame index
            instr_2_text.tStart = t  # local t and not account for scr refresh
            instr_2_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_2_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instr_2_text.started')
            # update status
            instr_2_text.status = STARTED
            instr_2_text.setAutoDraw(True)
        
        # if instr_2_text is active this frame...
        if instr_2_text.status == STARTED:
            # update params
            pass
        
        # *instr_2_resp* updates
        waitOnFlip = False
        
        # if instr_2_resp is starting this frame...
        if instr_2_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_2_resp.frameNStart = frameN  # exact frame index
            instr_2_resp.tStart = t  # local t and not account for scr refresh
            instr_2_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_2_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instr_2_resp.started')
            # update status
            instr_2_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instr_2_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instr_2_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instr_2_resp.status == STARTED and not waitOnFlip:
            theseKeys = instr_2_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _instr_2_resp_allKeys.extend(theseKeys)
            if len(_instr_2_resp_allKeys):
                instr_2_resp.keys = _instr_2_resp_allKeys[-1].name  # just the last key pressed
                instr_2_resp.rt = _instr_2_resp_allKeys[-1].rt
                instr_2_resp.duration = _instr_2_resp_allKeys[-1].duration
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
        for thisComponent in instr_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instr_2" ---
    for thisComponent in instr_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instr_2.stopped', globalClock.getTime(format='float'))
    # check responses
    if instr_2_resp.keys in ['', [], None]:  # No response was made
        instr_2_resp.keys = None
    thisExp.addData('instr_2_resp.keys',instr_2_resp.keys)
    if instr_2_resp.keys != None:  # we had a response
        thisExp.addData('instr_2_resp.rt', instr_2_resp.rt)
        thisExp.addData('instr_2_resp.duration', instr_2_resp.duration)
    thisExp.nextEntry()
    # the Routine "instr_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instr_3" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instr_3.started', globalClock.getTime(format='float'))
    # create starting attributes for instr_3_resp
    instr_3_resp.keys = []
    instr_3_resp.rt = []
    _instr_3_resp_allKeys = []
    # keep track of which components have finished
    instr_3Components = [instr_3_text, instr_3_resp]
    for thisComponent in instr_3Components:
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
    
    # --- Run Routine "instr_3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_3_text* updates
        
        # if instr_3_text is starting this frame...
        if instr_3_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_3_text.frameNStart = frameN  # exact frame index
            instr_3_text.tStart = t  # local t and not account for scr refresh
            instr_3_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_3_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instr_3_text.started')
            # update status
            instr_3_text.status = STARTED
            instr_3_text.setAutoDraw(True)
        
        # if instr_3_text is active this frame...
        if instr_3_text.status == STARTED:
            # update params
            pass
        
        # *instr_3_resp* updates
        waitOnFlip = False
        
        # if instr_3_resp is starting this frame...
        if instr_3_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_3_resp.frameNStart = frameN  # exact frame index
            instr_3_resp.tStart = t  # local t and not account for scr refresh
            instr_3_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_3_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instr_3_resp.started')
            # update status
            instr_3_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instr_3_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instr_3_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instr_3_resp.status == STARTED and not waitOnFlip:
            theseKeys = instr_3_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _instr_3_resp_allKeys.extend(theseKeys)
            if len(_instr_3_resp_allKeys):
                instr_3_resp.keys = _instr_3_resp_allKeys[-1].name  # just the last key pressed
                instr_3_resp.rt = _instr_3_resp_allKeys[-1].rt
                instr_3_resp.duration = _instr_3_resp_allKeys[-1].duration
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
        for thisComponent in instr_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instr_3" ---
    for thisComponent in instr_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instr_3.stopped', globalClock.getTime(format='float'))
    # check responses
    if instr_3_resp.keys in ['', [], None]:  # No response was made
        instr_3_resp.keys = None
    thisExp.addData('instr_3_resp.keys',instr_3_resp.keys)
    if instr_3_resp.keys != None:  # we had a response
        thisExp.addData('instr_3_resp.rt', instr_3_resp.rt)
        thisExp.addData('instr_3_resp.duration', instr_3_resp.duration)
    thisExp.nextEntry()
    # the Routine "instr_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "practice_rating" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('practice_rating.started', globalClock.getTime(format='float'))
    practice_slider.reset()
    # keep track of which components have finished
    practice_ratingComponents = [practice_text, practice_slider]
    for thisComponent in practice_ratingComponents:
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
    
    # --- Run Routine "practice_rating" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *practice_text* updates
        
        # if practice_text is starting this frame...
        if practice_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_text.frameNStart = frameN  # exact frame index
            practice_text.tStart = t  # local t and not account for scr refresh
            practice_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_text.started')
            # update status
            practice_text.status = STARTED
            practice_text.setAutoDraw(True)
        
        # if practice_text is active this frame...
        if practice_text.status == STARTED:
            # update params
            pass
        # *practice_slider* updates
        
        # if practice_slider is starting this frame...
        if practice_slider.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_slider.frameNStart = frameN  # exact frame index
            practice_slider.tStart = t  # local t and not account for scr refresh
            practice_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_slider, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('practice_slider.started', t)
            # update status
            practice_slider.status = STARTED
            practice_slider.setAutoDraw(True)
        continueRoutine &= practice_slider.noResponse  # a response ends the trial
        
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
        for thisComponent in practice_ratingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice_rating" ---
    for thisComponent in practice_ratingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('practice_rating.stopped', globalClock.getTime(format='float'))
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('practice_slider.response', practice_slider.getRating())
    thisExp.addData('practice_slider.rt', practice_slider.getRT())
    thisExp.nextEntry()
    # the Routine "practice_rating" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "practice_prating_int" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('practice_prating_int.started', globalClock.getTime(format='float'))
    practice_pain_slider.reset()
    # keep track of which components have finished
    practice_prating_intComponents = [pain_text_practice, practice_pain_slider]
    for thisComponent in practice_prating_intComponents:
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
    
    # --- Run Routine "practice_prating_int" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pain_text_practice* updates
        
        # if pain_text_practice is starting this frame...
        if pain_text_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pain_text_practice.frameNStart = frameN  # exact frame index
            pain_text_practice.tStart = t  # local t and not account for scr refresh
            pain_text_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pain_text_practice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pain_text_practice.started')
            # update status
            pain_text_practice.status = STARTED
            pain_text_practice.setAutoDraw(True)
        
        # if pain_text_practice is active this frame...
        if pain_text_practice.status == STARTED:
            # update params
            pass
        # *practice_pain_slider* updates
        
        # if practice_pain_slider is starting this frame...
        if practice_pain_slider.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_pain_slider.frameNStart = frameN  # exact frame index
            practice_pain_slider.tStart = t  # local t and not account for scr refresh
            practice_pain_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_pain_slider, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('practice_pain_slider.started', t)
            # update status
            practice_pain_slider.status = STARTED
            practice_pain_slider.setAutoDraw(True)
        continueRoutine &= practice_pain_slider.noResponse  # a response ends the trial
        
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
        for thisComponent in practice_prating_intComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice_prating_int" ---
    for thisComponent in practice_prating_intComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('practice_prating_int.stopped', globalClock.getTime(format='float'))
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('practice_pain_slider.response', practice_pain_slider.getRating())
    thisExp.addData('practice_pain_slider.rt', practice_pain_slider.getRT())
    thisExp.nextEntry()
    # the Routine "practice_prating_int" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "practice_prating_unpl" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('practice_prating_unpl.started', globalClock.getTime(format='float'))
    practice_pain_slider_2.reset()
    # keep track of which components have finished
    practice_prating_unplComponents = [pain_text_practice_2, practice_pain_slider_2]
    for thisComponent in practice_prating_unplComponents:
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
    
    # --- Run Routine "practice_prating_unpl" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pain_text_practice_2* updates
        
        # if pain_text_practice_2 is starting this frame...
        if pain_text_practice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pain_text_practice_2.frameNStart = frameN  # exact frame index
            pain_text_practice_2.tStart = t  # local t and not account for scr refresh
            pain_text_practice_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pain_text_practice_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pain_text_practice_2.started')
            # update status
            pain_text_practice_2.status = STARTED
            pain_text_practice_2.setAutoDraw(True)
        
        # if pain_text_practice_2 is active this frame...
        if pain_text_practice_2.status == STARTED:
            # update params
            pass
        # *practice_pain_slider_2* updates
        
        # if practice_pain_slider_2 is starting this frame...
        if practice_pain_slider_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_pain_slider_2.frameNStart = frameN  # exact frame index
            practice_pain_slider_2.tStart = t  # local t and not account for scr refresh
            practice_pain_slider_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_pain_slider_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('practice_pain_slider_2.started', t)
            # update status
            practice_pain_slider_2.status = STARTED
            practice_pain_slider_2.setAutoDraw(True)
        continueRoutine &= practice_pain_slider_2.noResponse  # a response ends the trial
        
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
        for thisComponent in practice_prating_unplComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice_prating_unpl" ---
    for thisComponent in practice_prating_unplComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('practice_prating_unpl.stopped', globalClock.getTime(format='float'))
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('practice_pain_slider_2.response', practice_pain_slider_2.getRating())
    thisExp.addData('practice_pain_slider_2.rt', practice_pain_slider_2.getRT())
    thisExp.nextEntry()
    # the Routine "practice_prating_unpl" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instr_experimentator" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instr_experimentator.started', globalClock.getTime(format='float'))
    # create starting attributes for instr_e_resp
    instr_e_resp.keys = []
    instr_e_resp.rt = []
    _instr_e_resp_allKeys = []
    # Run 'Begin Routine' code from acq_start_code
    print("Press G to continue!")
    # keep track of which components have finished
    instr_experimentatorComponents = [instr_e_text, instr_e_resp]
    for thisComponent in instr_experimentatorComponents:
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
    
    # --- Run Routine "instr_experimentator" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_e_text* updates
        
        # if instr_e_text is starting this frame...
        if instr_e_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_e_text.frameNStart = frameN  # exact frame index
            instr_e_text.tStart = t  # local t and not account for scr refresh
            instr_e_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_e_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instr_e_text.started')
            # update status
            instr_e_text.status = STARTED
            instr_e_text.setAutoDraw(True)
        
        # if instr_e_text is active this frame...
        if instr_e_text.status == STARTED:
            # update params
            pass
        
        # *instr_e_resp* updates
        waitOnFlip = False
        
        # if instr_e_resp is starting this frame...
        if instr_e_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_e_resp.frameNStart = frameN  # exact frame index
            instr_e_resp.tStart = t  # local t and not account for scr refresh
            instr_e_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_e_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instr_e_resp.started')
            # update status
            instr_e_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instr_e_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instr_e_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instr_e_resp.status == STARTED and not waitOnFlip:
            theseKeys = instr_e_resp.getKeys(keyList=['g'], ignoreKeys=["escape"], waitRelease=False)
            _instr_e_resp_allKeys.extend(theseKeys)
            if len(_instr_e_resp_allKeys):
                instr_e_resp.keys = _instr_e_resp_allKeys[-1].name  # just the last key pressed
                instr_e_resp.rt = _instr_e_resp_allKeys[-1].rt
                instr_e_resp.duration = _instr_e_resp_allKeys[-1].duration
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
        for thisComponent in instr_experimentatorComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instr_experimentator" ---
    for thisComponent in instr_experimentatorComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instr_experimentator.stopped', globalClock.getTime(format='float'))
    # check responses
    if instr_e_resp.keys in ['', [], None]:  # No response was made
        instr_e_resp.keys = None
    thisExp.addData('instr_e_resp.keys',instr_e_resp.keys)
    if instr_e_resp.keys != None:  # we had a response
        thisExp.addData('instr_e_resp.rt', instr_e_resp.rt)
        thisExp.addData('instr_e_resp.duration', instr_e_resp.duration)
    # Run 'End Routine' code from acq_start_code
    print("Start of Acquisiton!")
    thisExp.nextEntry()
    # the Routine "instr_experimentator" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    full_acq = data.TrialHandler(nReps=2, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='full_acq')
    thisExp.addLoop(full_acq)  # add the loop to the experiment
    thisFull_acq = full_acq.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFull_acq.rgb)
    if thisFull_acq != None:
        for paramName in thisFull_acq:
            globals()[paramName] = thisFull_acq[paramName]
    
    for thisFull_acq in full_acq:
        currentLoop = full_acq
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisFull_acq.rgb)
        if thisFull_acq != None:
            for paramName in thisFull_acq:
                globals()[paramName] = thisFull_acq[paramName]
        
        # set up handler to look after randomisation of conditions etc
        acq = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions("sequences/acq_"+expInfo['order']+".xlsx"),
            seed=None, name='acq')
        thisExp.addLoop(acq)  # add the loop to the experiment
        thisAcq = acq.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisAcq.rgb)
        if thisAcq != None:
            for paramName in thisAcq:
                globals()[paramName] = thisAcq[paramName]
        
        for thisAcq in acq:
            currentLoop = acq
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisAcq.rgb)
            if thisAcq != None:
                for paramName in thisAcq:
                    globals()[paramName] = thisAcq[paramName]
            
            # --- Prepare to start Routine "iti" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('iti.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from iti_code
            iti_duration = 3+random()*(5-3)
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
            while continueRoutine:
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
                    if tThisFlipGlobal > iti_text.tStartRefresh + iti_duration-frameTolerance:
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
            # the Routine "iti" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "stim_acq" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('stim_acq.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from marker_code_acq
            if cs == "CSp":
                print("Trial " + str(trial_i) + ": CS+")
            if cs == "CSm":
                print("Trial " + str(trial_i) + ": CS-")
            
            if us == 1:
                print('Shock')
                
            
            
            stim.setOri(orientation)
            # keep track of which components have finished
            stim_acqComponents = [stim, p_port]
            for thisComponent in stim_acqComponents:
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
            
            # --- Run Routine "stim_acq" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 3.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *stim* updates
                
                # if stim is starting this frame...
                if stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    stim.frameNStart = frameN  # exact frame index
                    stim.tStart = t  # local t and not account for scr refresh
                    stim.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stim, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stim.started')
                    # update status
                    stim.status = STARTED
                    stim.setAutoDraw(True)
                
                # if stim is active this frame...
                if stim.status == STARTED:
                    # update params
                    pass
                
                # if stim is stopping this frame...
                if stim.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > stim.tStartRefresh + 3.0-frameTolerance:
                        # keep track of stop time/frame for later
                        stim.tStop = t  # not accounting for scr refresh
                        stim.tStopRefresh = tThisFlipGlobal  # on global time
                        stim.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'stim.stopped')
                        # update status
                        stim.status = FINISHED
                        stim.setAutoDraw(False)
                # *p_port* updates
                
                # if p_port is starting this frame...
                if p_port.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    p_port.frameNStart = frameN  # exact frame index
                    p_port.tStart = t  # local t and not account for scr refresh
                    p_port.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(p_port, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('p_port.started', t)
                    # update status
                    p_port.status = STARTED
                    p_port.status = STARTED
                    win.callOnFlip(p_port.setData, int(cs_trigger))
                
                # if p_port is stopping this frame...
                if p_port.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > p_port.tStartRefresh + 0.005-frameTolerance:
                        # keep track of stop time/frame for later
                        p_port.tStop = t  # not accounting for scr refresh
                        p_port.tStopRefresh = tThisFlipGlobal  # on global time
                        p_port.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.addData('p_port.stopped', t)
                        # update status
                        p_port.status = FINISHED
                        win.callOnFlip(p_port.setData, int(0))
                
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
                for thisComponent in stim_acqComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "stim_acq" ---
            for thisComponent in stim_acqComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('stim_acq.stopped', globalClock.getTime(format='float'))
            # Run 'End Routine' code from marker_code_acq
            trial_i = trial_i + 1
            
            if p_port.status == STARTED:
                win.callOnFlip(p_port.setData, int(0))
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-3.000000)
            
            # --- Prepare to start Routine "us" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('us.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from us_code
            sendTrigger(us_trigger)
            # keep track of which components have finished
            usComponents = []
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
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
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
            # the Routine "us" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1 repeats of 'acq'
        
        
        # set up handler to look after randomisation of conditions etc
        acq_rating_trials = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions("sequences/acq_"+expInfo['order']+"_rating.xlsx"),
            seed=None, name='acq_rating_trials')
        thisExp.addLoop(acq_rating_trials)  # add the loop to the experiment
        thisAcq_rating_trial = acq_rating_trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisAcq_rating_trial.rgb)
        if thisAcq_rating_trial != None:
            for paramName in thisAcq_rating_trial:
                globals()[paramName] = thisAcq_rating_trial[paramName]
        
        for thisAcq_rating_trial in acq_rating_trials:
            currentLoop = acq_rating_trials
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisAcq_rating_trial.rgb)
            if thisAcq_rating_trial != None:
                for paramName in thisAcq_rating_trial:
                    globals()[paramName] = thisAcq_rating_trial[paramName]
            
            # --- Prepare to start Routine "short_iti" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('short_iti.started', globalClock.getTime(format='float'))
            # keep track of which components have finished
            short_itiComponents = [short_iti_text]
            for thisComponent in short_itiComponents:
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
            
            # --- Run Routine "short_iti" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *short_iti_text* updates
                
                # if short_iti_text is starting this frame...
                if short_iti_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    short_iti_text.frameNStart = frameN  # exact frame index
                    short_iti_text.tStart = t  # local t and not account for scr refresh
                    short_iti_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(short_iti_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'short_iti_text.started')
                    # update status
                    short_iti_text.status = STARTED
                    short_iti_text.setAutoDraw(True)
                
                # if short_iti_text is active this frame...
                if short_iti_text.status == STARTED:
                    # update params
                    pass
                
                # if short_iti_text is stopping this frame...
                if short_iti_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > short_iti_text.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        short_iti_text.tStop = t  # not accounting for scr refresh
                        short_iti_text.tStopRefresh = tThisFlipGlobal  # on global time
                        short_iti_text.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'short_iti_text.stopped')
                        # update status
                        short_iti_text.status = FINISHED
                        short_iti_text.setAutoDraw(False)
                
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
                for thisComponent in short_itiComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "short_iti" ---
            for thisComponent in short_itiComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('short_iti.stopped', globalClock.getTime(format='float'))
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.500000)
            
            # --- Prepare to start Routine "ratings" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('ratings.started', globalClock.getTime(format='float'))
            rating_polygon.setOri(orientation)
            cs_rating.reset()
            # keep track of which components have finished
            ratingsComponents = [rating_polygon, cs_rating]
            for thisComponent in ratingsComponents:
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
            
            # --- Run Routine "ratings" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *rating_polygon* updates
                
                # if rating_polygon is starting this frame...
                if rating_polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rating_polygon.frameNStart = frameN  # exact frame index
                    rating_polygon.tStart = t  # local t and not account for scr refresh
                    rating_polygon.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rating_polygon, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'rating_polygon.started')
                    # update status
                    rating_polygon.status = STARTED
                    rating_polygon.setAutoDraw(True)
                
                # if rating_polygon is active this frame...
                if rating_polygon.status == STARTED:
                    # update params
                    pass
                # *cs_rating* updates
                
                # if cs_rating is starting this frame...
                if cs_rating.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    cs_rating.frameNStart = frameN  # exact frame index
                    cs_rating.tStart = t  # local t and not account for scr refresh
                    cs_rating.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(cs_rating, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('cs_rating.started', t)
                    # update status
                    cs_rating.status = STARTED
                    cs_rating.setAutoDraw(True)
                continueRoutine &= cs_rating.noResponse  # a response ends the trial
                
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
                for thisComponent in ratingsComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ratings" ---
            for thisComponent in ratingsComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('ratings.stopped', globalClock.getTime(format='float'))
            # store data for acq_rating_trials (TrialHandler)
            acq_rating_trials.addData('cs_rating.response', cs_rating.getRating())
            acq_rating_trials.addData('cs_rating.rt', cs_rating.getRT())
            # Run 'End Routine' code from code
            print("Ratings")
            # the Routine "ratings" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1 repeats of 'acq_rating_trials'
        
        
        # --- Prepare to start Routine "pain_ratining_intensity" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('pain_ratining_intensity.started', globalClock.getTime(format='float'))
        p_rating_1.reset()
        # keep track of which components have finished
        pain_ratining_intensityComponents = [p_rating_1]
        for thisComponent in pain_ratining_intensityComponents:
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
        
        # --- Run Routine "pain_ratining_intensity" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *p_rating_1* updates
            
            # if p_rating_1 is starting this frame...
            if p_rating_1.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                p_rating_1.frameNStart = frameN  # exact frame index
                p_rating_1.tStart = t  # local t and not account for scr refresh
                p_rating_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(p_rating_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('p_rating_1.started', t)
                # update status
                p_rating_1.status = STARTED
                p_rating_1.setAutoDraw(True)
            continueRoutine &= p_rating_1.noResponse  # a response ends the trial
            
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
            for thisComponent in pain_ratining_intensityComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "pain_ratining_intensity" ---
        for thisComponent in pain_ratining_intensityComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('pain_ratining_intensity.stopped', globalClock.getTime(format='float'))
        # store data for full_acq (TrialHandler)
        full_acq.addData('p_rating_1.response', p_rating_1.getRating())
        full_acq.addData('p_rating_1.rt', p_rating_1.getRT())
        # the Routine "pain_ratining_intensity" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "paint_ratining_unpleasant" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('paint_ratining_unpleasant.started', globalClock.getTime(format='float'))
        p_rating_2.reset()
        # keep track of which components have finished
        paint_ratining_unpleasantComponents = [p_rating_2]
        for thisComponent in paint_ratining_unpleasantComponents:
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
        
        # --- Run Routine "paint_ratining_unpleasant" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *p_rating_2* updates
            
            # if p_rating_2 is starting this frame...
            if p_rating_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                p_rating_2.frameNStart = frameN  # exact frame index
                p_rating_2.tStart = t  # local t and not account for scr refresh
                p_rating_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(p_rating_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('p_rating_2.started', t)
                # update status
                p_rating_2.status = STARTED
                p_rating_2.setAutoDraw(True)
            continueRoutine &= p_rating_2.noResponse  # a response ends the trial
            
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
            for thisComponent in paint_ratining_unpleasantComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "paint_ratining_unpleasant" ---
        for thisComponent in paint_ratining_unpleasantComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('paint_ratining_unpleasant.stopped', globalClock.getTime(format='float'))
        # store data for full_acq (TrialHandler)
        full_acq.addData('p_rating_2.response', p_rating_2.getRating())
        full_acq.addData('p_rating_2.rt', p_rating_2.getRT())
        # the Routine "paint_ratining_unpleasant" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 2 repeats of 'full_acq'
    
    
    # set up handler to look after randomisation of conditions etc
    full_ext = data.TrialHandler(nReps=2, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='full_ext')
    thisExp.addLoop(full_ext)  # add the loop to the experiment
    thisFull_ext = full_ext.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFull_ext.rgb)
    if thisFull_ext != None:
        for paramName in thisFull_ext:
            globals()[paramName] = thisFull_ext[paramName]
    
    for thisFull_ext in full_ext:
        currentLoop = full_ext
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisFull_ext.rgb)
        if thisFull_ext != None:
            for paramName in thisFull_ext:
                globals()[paramName] = thisFull_ext[paramName]
        
        # set up handler to look after randomisation of conditions etc
        ext = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions("sequences/ext_"+expInfo['order']+".xlsx"),
            seed=None, name='ext')
        thisExp.addLoop(ext)  # add the loop to the experiment
        thisExt = ext.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisExt.rgb)
        if thisExt != None:
            for paramName in thisExt:
                globals()[paramName] = thisExt[paramName]
        
        for thisExt in ext:
            currentLoop = ext
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisExt.rgb)
            if thisExt != None:
                for paramName in thisExt:
                    globals()[paramName] = thisExt[paramName]
            
            # --- Prepare to start Routine "iti" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('iti.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from iti_code
            iti_duration = 3+random()*(5-3)
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
            while continueRoutine:
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
                    if tThisFlipGlobal > iti_text.tStartRefresh + iti_duration-frameTolerance:
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
            # the Routine "iti" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "stim_ext" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('stim_ext.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from marker_code_ext
            if cs == "CSp":
                print("Trial " + str(trial_i) + ": CS+")
            if cs == "CSm":
                print("Trial " + str(trial_i) + ": CS-")
            
            stim_2.setOri(orientation)
            # keep track of which components have finished
            stim_extComponents = [stim_2, p_port_2]
            for thisComponent in stim_extComponents:
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
            
            # --- Run Routine "stim_ext" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 3.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *stim_2* updates
                
                # if stim_2 is starting this frame...
                if stim_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    stim_2.frameNStart = frameN  # exact frame index
                    stim_2.tStart = t  # local t and not account for scr refresh
                    stim_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stim_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stim_2.started')
                    # update status
                    stim_2.status = STARTED
                    stim_2.setAutoDraw(True)
                
                # if stim_2 is active this frame...
                if stim_2.status == STARTED:
                    # update params
                    pass
                
                # if stim_2 is stopping this frame...
                if stim_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > stim_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        stim_2.tStop = t  # not accounting for scr refresh
                        stim_2.tStopRefresh = tThisFlipGlobal  # on global time
                        stim_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'stim_2.stopped')
                        # update status
                        stim_2.status = FINISHED
                        stim_2.setAutoDraw(False)
                # *p_port_2* updates
                
                # if p_port_2 is starting this frame...
                if p_port_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    p_port_2.frameNStart = frameN  # exact frame index
                    p_port_2.tStart = t  # local t and not account for scr refresh
                    p_port_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(p_port_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('p_port_2.started', t)
                    # update status
                    p_port_2.status = STARTED
                    p_port_2.status = STARTED
                    win.callOnFlip(p_port_2.setData, int(cs_trigger))
                
                # if p_port_2 is stopping this frame...
                if p_port_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > p_port_2.tStartRefresh + 0.005-frameTolerance:
                        # keep track of stop time/frame for later
                        p_port_2.tStop = t  # not accounting for scr refresh
                        p_port_2.tStopRefresh = tThisFlipGlobal  # on global time
                        p_port_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.addData('p_port_2.stopped', t)
                        # update status
                        p_port_2.status = FINISHED
                        win.callOnFlip(p_port_2.setData, int(0))
                
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
                for thisComponent in stim_extComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "stim_ext" ---
            for thisComponent in stim_extComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('stim_ext.stopped', globalClock.getTime(format='float'))
            # Run 'End Routine' code from marker_code_ext
            trial_i = trial_i + 1
            
            if p_port_2.status == STARTED:
                win.callOnFlip(p_port_2.setData, int(0))
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-3.000000)
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1 repeats of 'ext'
        
        
        # set up handler to look after randomisation of conditions etc
        ext_rating_trials = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions("sequences/ext_"+expInfo['order']+"_rating.xlsx"),
            seed=None, name='ext_rating_trials')
        thisExp.addLoop(ext_rating_trials)  # add the loop to the experiment
        thisExt_rating_trial = ext_rating_trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisExt_rating_trial.rgb)
        if thisExt_rating_trial != None:
            for paramName in thisExt_rating_trial:
                globals()[paramName] = thisExt_rating_trial[paramName]
        
        for thisExt_rating_trial in ext_rating_trials:
            currentLoop = ext_rating_trials
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisExt_rating_trial.rgb)
            if thisExt_rating_trial != None:
                for paramName in thisExt_rating_trial:
                    globals()[paramName] = thisExt_rating_trial[paramName]
            
            # --- Prepare to start Routine "short_iti" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('short_iti.started', globalClock.getTime(format='float'))
            # keep track of which components have finished
            short_itiComponents = [short_iti_text]
            for thisComponent in short_itiComponents:
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
            
            # --- Run Routine "short_iti" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *short_iti_text* updates
                
                # if short_iti_text is starting this frame...
                if short_iti_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    short_iti_text.frameNStart = frameN  # exact frame index
                    short_iti_text.tStart = t  # local t and not account for scr refresh
                    short_iti_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(short_iti_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'short_iti_text.started')
                    # update status
                    short_iti_text.status = STARTED
                    short_iti_text.setAutoDraw(True)
                
                # if short_iti_text is active this frame...
                if short_iti_text.status == STARTED:
                    # update params
                    pass
                
                # if short_iti_text is stopping this frame...
                if short_iti_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > short_iti_text.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        short_iti_text.tStop = t  # not accounting for scr refresh
                        short_iti_text.tStopRefresh = tThisFlipGlobal  # on global time
                        short_iti_text.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'short_iti_text.stopped')
                        # update status
                        short_iti_text.status = FINISHED
                        short_iti_text.setAutoDraw(False)
                
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
                for thisComponent in short_itiComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "short_iti" ---
            for thisComponent in short_itiComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('short_iti.stopped', globalClock.getTime(format='float'))
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.500000)
            
            # --- Prepare to start Routine "ratings" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('ratings.started', globalClock.getTime(format='float'))
            rating_polygon.setOri(orientation)
            cs_rating.reset()
            # keep track of which components have finished
            ratingsComponents = [rating_polygon, cs_rating]
            for thisComponent in ratingsComponents:
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
            
            # --- Run Routine "ratings" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *rating_polygon* updates
                
                # if rating_polygon is starting this frame...
                if rating_polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rating_polygon.frameNStart = frameN  # exact frame index
                    rating_polygon.tStart = t  # local t and not account for scr refresh
                    rating_polygon.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rating_polygon, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'rating_polygon.started')
                    # update status
                    rating_polygon.status = STARTED
                    rating_polygon.setAutoDraw(True)
                
                # if rating_polygon is active this frame...
                if rating_polygon.status == STARTED:
                    # update params
                    pass
                # *cs_rating* updates
                
                # if cs_rating is starting this frame...
                if cs_rating.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    cs_rating.frameNStart = frameN  # exact frame index
                    cs_rating.tStart = t  # local t and not account for scr refresh
                    cs_rating.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(cs_rating, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('cs_rating.started', t)
                    # update status
                    cs_rating.status = STARTED
                    cs_rating.setAutoDraw(True)
                continueRoutine &= cs_rating.noResponse  # a response ends the trial
                
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
                for thisComponent in ratingsComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ratings" ---
            for thisComponent in ratingsComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('ratings.stopped', globalClock.getTime(format='float'))
            # store data for ext_rating_trials (TrialHandler)
            ext_rating_trials.addData('cs_rating.response', cs_rating.getRating())
            ext_rating_trials.addData('cs_rating.rt', cs_rating.getRT())
            # Run 'End Routine' code from code
            print("Ratings")
            # the Routine "ratings" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1 repeats of 'ext_rating_trials'
        
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 2 repeats of 'full_ext'
    
    
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
