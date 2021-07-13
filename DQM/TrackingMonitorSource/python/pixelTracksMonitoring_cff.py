import FWCore.ParameterSet.Config as cms

from DQM.TrackingMonitor.TrackerCollisionTrackingMonitor_cfi import *
pixelTracksMonitor = TrackerCollisionTrackMon.clone(
    FolderName = 'Tracking/PixelTrackParameters/pixelTracks',
    TrackProducer = 'pixelTracks',
    allTrackProducer = 'pixelTracks',
    beamSpot = 'offlineBeamSpot',
    primaryVertex = 'pixelVertices',
    pvNDOF = 1,
    doAllPlots = True,
    doLumiAnalysis = True,
    doProfilesVsLS = True,
    doDCAPlots = True,
    doEffFromHitPatternVsPU = False,
    doEffFromHitPatternVsBX = False,
    doEffFromHitPatternVsLUMI = False,
    doPlotsVsGoodPVtx = True,
    doPlotsVsLUMI = True,
    doPlotsVsBX = True
)

_trackSelector = cms.EDFilter('TrackSelector',
    src = cms.InputTag('pixelTracks'),
    cut = cms.string("")
)

pixelTracksPt0to1 = _trackSelector.clone(cut = "pt >= 0 & pt < 1 ")
pixelTracksPt1 = _trackSelector.clone(cut = "pt >= 1 ")
from DQM.TrackingMonitorSource.TrackCollections2monitor_cff import highPurityPV0p1 as _highPurityPV0p1
pixelTracksPV0p1 = _highPurityPV0p1.clone(
    src = "pixelTracks",
    quality = "",
    vertexTag = "goodPixelVertices"
)

pixelTracksMonitorPt0to1 = pixelTracksMonitor.clone(
    TrackProducer = "pixelTracksPt0to1",
    FolderName = "Tracking/PixelTrackParameters/pt_0to1"
)
pixelTracksMonitorPt1 = pixelTracksMonitor.clone(
    TrackProducer = "pixelTracksPt1",
    FolderName = "Tracking/PixelTrackParameters/pt_1"
)
pixelTracksMonitorPV0p1 = pixelTracksMonitor.clone(
    TrackProducer = "pixelTracksPV0p1",
    FolderName = "Tracking/PixelTrackParameters/dzPV0p1"
)


from CommonTools.ParticleFlow.goodOfflinePrimaryVertices_cfi import goodOfflinePrimaryVertices as _goodOfflinePrimaryVertices
goodPixelVertices = _goodOfflinePrimaryVertices.clone(
    src = "pixelVertices"
)

from DQM.TrackingMonitor.primaryVertexResolution_cfi import primaryVertexResolution as _primaryVertexResolution
pixelVertexResolution = _primaryVertexResolution.clone(
    vertexSrc = "goodPixelVertices",
    rootFolder = "OfflinePixelPV/Resolution"
)

pixelTracksMonitoringTask = cms.Task(
    goodPixelVertices,
    pixelTracksPt0to1,
    pixelTracksPt1,
    pixelTracksPV0p1,
)

pixelTracksMonitoring = cms.Sequence(
    pixelTracksMonitor +
    pixelTracksMonitorPt0to1 +
    pixelTracksMonitorPt1 +
    pixelTracksMonitorPV0p1 +
    pixelVertexResolution,
    pixelTracksMonitoringTask
)
