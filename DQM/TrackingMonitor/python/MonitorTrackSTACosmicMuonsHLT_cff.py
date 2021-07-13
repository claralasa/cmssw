import FWCore.ParameterSet.Config as cms

from DQM.TrackingMonitor.MonitorTrackSTAMuons_cfi import *
MonitorTrackSTACosmicMuonsHLTDT = MonitorTrackSTAMuons.clone(
    TrackProducer = 'dtCosmicSTA',
    FolderName = 'Muons/cosmicMuonsHLTDT'
)
from DQM.TrackingMonitor.MonitorTrackSTAMuons_cfi import *
MonitorTrackSTACosmicMuonsHLTCSC = MonitorTrackSTAMuons.clone(
    TrackProducer = 'cscCosmicSTA',
    FolderName = 'Muons/cosmicMuonsHLTCSC'
)
