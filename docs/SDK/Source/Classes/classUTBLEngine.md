---
title: UTBLEngine
type: class
aliases: UTBLEngine
share: false

---

# UTBLEngine





Inherits from UGameEngine

## Public Functions

|                | Name           |
| -------------- | -------------- |
| float | **[[GetAvailableCPU]]**() |
| float | **[[GetStatFPS]]**() |
| float | **[[GetStatMS]]**() |
| | **[[UTBLEngine]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| UClass * | **[[CharacterCombatStatesClass]]**  |
| UClass * | **[[HorseClass]]**  |
| UClass * | **[[WeaponFistClass]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [FAvailableCPUBuckets](/docs/SDK/Source/Classes/structFAvailableCPUBuckets.md) | **[[AvailableCpu]]**  |
| [FAvailableCPUBuckets](/docs/SDK/Source/Classes/structFAvailableCPUBuckets.md) | **[[AvailableCpuEx]]**  |
| float | **[[AvailableCpuRatio]]**  |
| float | **[[AvailableCpuTimer]]**  |
| double | **[[AverageFrameTime]]**  |
| double | **[[AverageFrameTimePerMinute]]**  |
| double | **[[AveragePingTime]]**  |
| double | **[[AveragePingTimePerMinute]]**  |
| float | **[[CPUPerfIndex]]**  |
| [FFrameTimeBuckets](/docs/SDK/Source/Classes/structFFrameTimeBuckets.md) | **[[FrameTimeBuckets]]**  |
| float | **[[GPUPerfIndex]]**  |
| [FTBLHardwareInfo](/docs/SDK/Source/Classes/structFTBLHardwareInfo.md) | **[[HardwareInfo]]**  |
| double | **[[LastAutonomousMovementCorrectionTime]]**  |
| double | **[[LastFrameTime]]**  |
| uint64 | **[[LastFrameTimestamp]]**  |
| uint32 | **[[LastInOutOfOrderPackets]]**  |
| uint32 | **[[LastInPackets]]**  |
| uint32 | **[[LastInPacketsLost]]**  |
| double | **[[LastNetFlushTime]]**  |
| uint32 | **[[LastOutBytes]]**  |
| uint32 | **[[LastOutOutOfOrderPackets]]**  |
| uint32 | **[[LastOutPackets]]**  |
| uint32 | **[[LastOutPacketsLost]]**  |
| int32 | **[[LastSkippedServerMoveFrame]]**  |
| uint32 | **[[NetAutonomousMovementCorrectionBunches]]**  |
| uint32 | **[[NetAutonomousMovementCorrections]]**  |
| uint32 | **[[NetConnections]]**  |
| uint32 | **[[NetInOutOfOrderPackets]]**  |
| uint32 | **[[NetInPackets]]**  |
| uint32 | **[[NetInPacketsLost]]**  |
| uint64 | **[[NetOutBytes]]**  |
| uint32 | **[[NetOutOutOfOrderPackets]]**  |
| uint32 | **[[NetOutPackets]]**  |
| uint32 | **[[NetOutPacketsLost]]**  |
| double | **[[NetOutTime]]**  |
| uint32 | **[[NetSampleCount]]**  |
| int32 | **[[NetSaturatedCount]]**  |
| uint32 | **[[NetSimulatedMovementCorrections]]**  |
| TArray< [FPerMinuteBucket](/docs/SDK/Source/Classes/structFPerMinuteBucket.md) > | **[[PerMinuteBuckets]]**  |
| float | **[[PerMinuteTimer]]**  |
| int32 | **[[PingFrameNumber]]**  |
| [FPingTimeBuckets](/docs/SDK/Source/Classes/structFPingTimeBuckets.md) | **[[PingTimeBuckets]]**  |
| UWorld * | **[[ServerWorld]]**  |
| int32 | **[[SkippedServerMoveFrames]]**  |
| int32 | **[[SkippedServerMoves]]**  |
| [FFrameTimeBuckets](/docs/SDK/Source/Classes/structFFrameTimeBuckets.md) | **[[StatFrameTimeBuckets]]**  |
| int32 | **[[TotalFrames]]**  |
| int32 | **[[TotalFramesPerMinute]]**  |
| int32 | **[[TotalPingSamples]]**  |
| int32 | **[[TotalPingSamplesPerMinute]]**  |
| int64 | **[[TotalRetryReliableBytes]]**  |
| int64 | **[[TotalRetryReliableCount]]**  |
| int64 | **[[TotalRetryUnreliableBytes]]**  |
| int64 | **[[TotalRetryUnreliableCount]]**  |
| int64 | **[[TotalSendFailBytes]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200