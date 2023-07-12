---
title: FMovementDebugFrame
type: struct
aliases: FMovementDebugFrame
share: false

---

# FMovementDebugFrame





## Public Functions

|                | Name           |
| -------------- | -------------- |
| TBL_API | **[[FMovementDebugFrame]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| FVector | **[[Acceleration]]**  |
| float | **[[AdditionalTime]]**  |
| FVector | **[[AnimRootMotionVelocity]]**  |
| FName | **[[AttackName]]**  |
| int32 | **[[AutorunMovementMode]]**  |
| FRotator | **[[AutorunRotation]]**  |
| float | **[[AvailableCpuRatio]]**  |
| float | **[[AvailableCpuTimer]]**  |
| float | **[[AverageFrameTime]]**  |
| float | **[[AverageFrameTimePerMinute]]**  |
| float | **[[AveragePingTime]]**  |
| float | **[[AveragePingTimePerMinute]]**  |
| int32 | **[[CannotMove]]**  |
| float | **[[CapsuleHalfHeight]]**  |
| float | **[[CapsuleRadius]]**  |
| FVector | **[[CharacterLocation]]**  |
| int32 | **[[ClientAuthorativePosition]]**  |
| float | **[[ClientTimeStamp]]**  |
| FName | **[[CombatState]]**  |
| float | **[[CombatStateLength]]**  |
| FName | **[[CurrentFloor]]**  |
| int32 | **[[CustomMovementMode]]**  |
| [FDebugDrawShapes](/docs/SDK/Source/Classes/structFDebugDrawShapes.md) | **[[DebugDraw]]**  |
| [FDebugMovementReplication](/docs/SDK/Source/Classes/structFDebugMovementReplication.md) | **[[DebugMovementReplication]]**  |
| [FDebugTimeDiscrepancyDetection](/docs/SDK/Source/Classes/structFDebugTimeDiscrepancyDetection.md) | **[[DebugTimeDiscrepancyDetection]]**  |
| float | **[[DeltaTime]]**  |
| int32 | **[[FrameCounter]]**  |
| [FGameNetworkSettings](/docs/SDK/Source/Classes/structFGameNetworkSettings.md) | **[[GameNetworkSettings]]**  |
| [FHorseMovementDebugFrame](/docs/SDK/Source/Classes/structFHorseMovementDebugFrame.md) | **[[HorseMovement]]**  |
| TArray< [FMovementDebugInventoryItem](/docs/SDK/Source/Classes/structFMovementDebugInventoryItem.md) > | **[[InventoryItems]]**  |
| int32 | **[[IsOnLadder]]**  |
| float | **[[LastAutonomousMovementCorrectionTime]]**  |
| float | **[[LastCorrectionTimestamp]]**  |
| float | **[[LastFrameTime]]**  |
| float | **[[LastNetFlushTime]]**  |
| int32 | **[[LastSkippedServerMoveFrame]]**  |
| float | **[[LastSyncMovementTime]]**  |
| float | **[[LastTimeDiscrepancyDetectedTime]]**  |
| FVector | **[[Location]]**  |
| float | **[[LockMeshTurnLimit]]**  |
| float | **[[LockMeshYaw]]**  |
| float | **[[MaxErrorSquared]]**  |
| float | **[[MaxSpeed]]**  |
| TArray< [FAnimDebugMontageInstance](/docs/SDK/Source/Classes/structFAnimDebugMontageInstance.md) > | **[[MontageInstances]]**  |
| TArray< [FAnimDebugMontageInstance](/docs/SDK/Source/Classes/structFAnimDebugMontageInstance.md) > | **[[MontageInstances1p]]**  |
| TEnumAsByte< EMovementMode > | **[[MovementMode]]**  |
| [UMovementSequence](/docs/SDK/Source/Classes/classUMovementSequence.md) * | **[[MovementSequence]]**  |
| float | **[[MovementSpeed]]**  |
| int32 | **[[NetAutonomousMovementCorrectionBunches]]**  |
| int32 | **[[NetAutonomousMovementCorrections]]**  |
| int32 | **[[NetConnections]]**  |
| int32 | **[[NetInOutOfOrderPackets]]**  |
| int32 | **[[NetInPackets]]**  |
| int32 | **[[NetInPacketsLost]]**  |
| int32 | **[[NetOutOutOfOrderPackets]]**  |
| int32 | **[[NetOutPackets]]**  |
| int32 | **[[NetOutPacketsLost]]**  |
| int32 | **[[NetSaturatedCount]]**  |
| TArray< [FMovementDebugSimualated](/docs/SDK/Source/Classes/structFMovementDebugSimualated.md) > | **[[OtherCharacters]]**  |
| float | **[[Ping]]**  |
| FVector | **[[PreCorrectionLocation]]**  |
| FVector | **[[PreMoveVelocity]]**  |
| TArray< FString > | **[[PropertyDebuggerNames]]**  |
| TArray< FString > | **[[PropertyDebuggerValues]]**  |
| int32 | **[[RootMotion]]**  |
| FRotator | **[[Rotation]]**  |
| int32 | **[[SkippedServerMoveFrames]]**  |
| int32 | **[[SkippedServerMoves]]**  |
| FVector | **[[SplineLocation]]**  |
| float | **[[SprintSpeed]]**  |
| float | **[[StatFPS]]**  |
| float | **[[StatMS]]**  |
| TArray< [FMovementDebugSyncEvent](/docs/SDK/Source/Classes/structFMovementDebugSyncEvent.md) > | **[[SyncEvents]]**  |
| float | **[[TimeBetweenDiscrepancyDetected]]**  |
| float | **[[TimeInCombatState]]**  |
| int32 | **[[TotalRetryReliableBytes]]**  |
| int32 | **[[TotalRetryReliableCount]]**  |
| int32 | **[[TotalRetryUnreliableBytes]]**  |
| int32 | **[[TotalRetryUnreliableCount]]**  |
| int32 | **[[TotalSendFailBytes]]**  |
| float | **[[TotalServerTime]]**  |
| float | **[[TracerEndTime]]**  |
| float | **[[TracerStartTime]]**  |
| FVector | **[[Velocity]]**  |
| int32 | **[[Version]]**  |
| float | **[[WorldTime]]**  |
| int32 | **[[bCinematicRestrictedControl]]**  |
| int32 | **[[bDidMovementCorrection]]**  |
| int32 | **[[bDidPossess]]**  |
| int32 | **[[bIsAutorunSprinting]]**  |
| int32 | **[[bIsFirstDualMove]]**  |
| int32 | **[[bIsForcedAutorun]]**  |
| int32 | **[[bIsSprintDecelerating]]**  |
| int32 | **[[bIsSprinting]]**  |
| int32 | **[[bLockMesh]]**  |
| int32 | **[[bMoveBackwardHeld]]**  |
| int32 | **[[bMoveForwardHeld]]**  |
| int32 | **[[bMoveLeftHeld]]**  |
| int32 | **[[bMoveRightHeld]]**  |
| int32 | **[[bSkipEvaluation]]**  |
| int32 | **[[bSkipUpdate]]**  |
| int32 | **[[bWantsToSprint]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:01 +0200