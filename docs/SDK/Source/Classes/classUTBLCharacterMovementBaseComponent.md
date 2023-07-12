---
title: UTBLCharacterMovementBaseComponent
type: class
aliases: UTBLCharacterMovementBaseComponent
share: false

---

# UTBLCharacterMovementBaseComponent





Inherits from UCharacterMovementComponent, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

Inherited by [USiegeEngineMovement](/docs/SDK/Source/Classes/classUSiegeEngineMovement.md), [UTBLCharacterMovement](/docs/SDK/Source/Classes/classUTBLCharacterMovement.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AuthorityForceAutorun]]**(const [FAutorunParams](/docs/SDK/Source/Classes/structFAutorunParams.md) & Params, [ATBLCharacterBase](/docs/SDK/Source/Classes/classATBLCharacterBase.md) * Leader) |
| void | **[[AuthoritySetAutorunMovementMode]]**(EAutorunMovementMode InMovementMode) |
| void | **[[AuthorityStopForcedAutorun]]**() |
| void | **[[ClientStopForcedAutorun]]**(uint8 SyncMovementId) |
| bool | **[[DidHitBottomOfCapsule]]**(const FHitResult & Hit) const |
| float | **[[GetAutorunStartTime]]**() const |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| TEnumAsByte< EMovementMode > | **[[GetMovementMode]]**() const |
| bool | **[[HasMovementAction]]**([UMovementSequence](/docs/SDK/Source/Classes/classUMovementSequence.md) * Sequence) const |
| bool | **[[IsInitialAutorun]]**() const |
| void | **[[LockForcedAutorun]]**(bool bLock) |
| void | **[[SetAllowPositionError]]**(bool InAllowPositionError) |
| | **[[UTBLCharacterMovementBaseComponent]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[BroadcastPlaySpawnAnimation]]**(FName Animation) |
| void | **[[BroadcastSetDowned]]**(bool bDowned) |
| void | **[[BroadcastStartMovement]]**(const [FMovementActionInitiationParams](/docs/SDK/Source/Classes/structFMovementActionInitiationParams.md) & InitParams) |
| void | **[[BroadcastStopMovement]]**([UMovementSequence](/docs/SDK/Source/Classes/classUMovementSequence.md) * Sequence, bool bExecuteClientFirst) |
| void | **[[ClientCinematicAllowControl]]**(uint8 SyncMovementId) |
| void | **[[ClientCinematicRestrictControl]]**(uint8 SyncMovementId) |
| void | **[[ClientSetAutorunMovementMode]]**(EAutorunMovementMode InMovementMode, uint8 SyncMovementId) |
| void | **[[ClientStartForcedAutorun]]**(const [FAutorunParams](/docs/SDK/Source/Classes/structFAutorunParams.md) & Params, uint8 SyncMovementId) |
| void | **[[ClientStartMovement]]**(const [FMovementActionInitiationParams](/docs/SDK/Source/Classes/structFMovementActionInitiationParams.md) & InitParams, uint8 SyncMovementId) |
| void | **[[InitialAutorunExpired]]**() |
| void | **[[NoStopAutorunExpired]]**() |
| void | **[[OnAutorunParamsChanged]]**() |
| void | **[[OnRep_AutorunParams]]**() |
| void | **[[OnRep_MovementAnimationEvent]]**() |
| void | **[[ServerAckMovement]]**(uint8 SyncMovementId, float ClientTimeStamp) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[BottomOfCapsuleHeight]]**  |
| USceneComponent * | **[[MasterTransformComponent]]**  |
| [FMovementMetrics](/docs/SDK/Source/Classes/structFMovementMetrics.md) | **[[MovementMetrics]]**  |
| float | **[[MovementSequenceStepUpX]]**  |
| float | **[[MovementSequenceStepUpZ]]**  |
| FInitialAutorunExpiredSignature | **[[OnInitialAutorunExpired]]**  |
| FMovementActionFinished | **[[OnMovementActionFinished]]**  |
| FMovementActionStarted | **[[OnMovementActionStarted]]**  |
| FVector | **[[PreCorrectionLocation]]**  |
| uint8 | **[[bIsPreMovement]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [UMovementInstance](/docs/SDK/Source/Classes/classUMovementInstance.md) * | **[[ActiveMovementAction]]**  |
| [FReplicated_FAutorunParams](/docs/SDK/Source/Classes/structFReplicated__FAutorunParams.md) | **[[AutorunParams]]**  |
| float | **[[AutorunStartTime]]**  |
| int32 | **[[CharacterControlInstanceId]]**  |
| TArray< [FCharacterControlInstance](/docs/SDK/Source/Classes/structFCharacterControlInstance.md) > | **[[CharacterControlInstances]]**  |
| TArray< [FCharacterControlOverTime](/docs/SDK/Source/Classes/structFCharacterControlOverTime.md) > | **[[CharacterControlOverTime]]**  |
| [FCharacterControlInstance](/docs/SDK/Source/Classes/structFCharacterControlInstance.md) | **[[CurrentCharacterControl]]**  |
| TArray< [FDebugVelocityGraphEntry](/docs/SDK/Source/Classes/structFDebugVelocityGraphEntry.md) > | **[[DebugVelocityGraph]]**  |
| [FDelayStartForcedAutorun](/docs/SDK/Source/Classes/structFDelayStartForcedAutorun.md) | **[[DelayStartForcedAutorun]]**  |
| int32 | **[[InitialAutorunHorizontalLock]]**  |
| FTimerHandle | **[[InitialAutorunTimerHandle]]**  |
| [FAutorunParams](/docs/SDK/Source/Classes/structFAutorunParams.md) | **[[LastAutorunParams]]**  |
| FRotator | **[[LastControlRotation]]**  |
| float | **[[LastMoveTime]]**  |
| [UMovementSequence](/docs/SDK/Source/Classes/classUMovementSequence.md) * | **[[LastMovementSequence]]**  |
| TEnumAsByte< EStartMovementResult::Type > | **[[LastStartMovementResult]]**  |
| float | **[[LastSyncMovementTime]]**  |
| float | **[[LastTimeDiscrepancyDetectedTime]]**  |
| TArray< [FDebugMovementAction](/docs/SDK/Source/Classes/structFDebugMovementAction.md) > | **[[LogPreviousMovements]]**  |
| [FReplicated_FMovementAnimationEvent](/docs/SDK/Source/Classes/structFReplicated__FMovementAnimationEvent.md) | **[[MovementAnimationEvent]]**  |
| uint8 | **[[NextSyncMovementId]]**  |
| int32 | **[[NoStopAutorunHorizontalLock]]**  |
| FTimerHandle | **[[NoStopAutorunTimerHandle]]**  |
| [FServerMoveParams](/docs/SDK/Source/Classes/structFServerMoveParams.md) | **[[ServerMoveParams]]**  |
| TMap< uint8, EAutorunMovementMode > | **[[SyncAutorunMovementMode]]**  |
| TMap< uint8, [FCombatStateCancelAttack](/docs/SDK/Source/Classes/structFCombatStateCancelAttack.md) > | **[[SyncCancelAttack]]**  |
| TMap< uint8, [FCombatStateChargeStab](/docs/SDK/Source/Classes/structFCombatStateChargeStab.md) > | **[[SyncChargeStab]]**  |
| TMap< uint8, [FDisableAttackRootMotion](/docs/SDK/Source/Classes/structFDisableAttackRootMotion.md) > | **[[SyncDisableAttackRootMotion]]**  |
| TMap< uint8, [FAutorunParams](/docs/SDK/Source/Classes/structFAutorunParams.md) > | **[[SyncForcedAutorunParams]]**  |
| TMap< uint8, [FCombatStateGetUp](/docs/SDK/Source/Classes/structFCombatStateGetUp.md) > | **[[SyncGetUp]]**  |
| TMap< uint8, [FServerHitWorldParams](/docs/SDK/Source/Classes/structFServerHitWorldParams.md) > | **[[SyncHitWorld]]**  |
| TMap< uint8, [FHorseToHorseBump](/docs/SDK/Source/Classes/structFHorseToHorseBump.md) > | **[[SyncHorseToHorseBump]]**  |
| TMap< uint8, [FHorseToWorldBump](/docs/SDK/Source/Classes/structFHorseToWorldBump.md) > | **[[SyncHorseToWorldBump]]**  |
| TMap< uint8, [FServerInitiateAbilityParams](/docs/SDK/Source/Classes/structFServerInitiateAbilityParams.md) > | **[[SyncInitiateAbility]]**  |
| TMap< uint8, [FManualReload](/docs/SDK/Source/Classes/structFManualReload.md) > | **[[SyncManualReload]]**  |
| TMap< uint8, [FMountLadder](/docs/SDK/Source/Classes/structFMountLadder.md) > | **[[SyncMountLadder]]**  |
| TArray< [FSyncMovementAction](/docs/SDK/Source/Classes/structFSyncMovementAction.md) > | **[[SyncMovementActions]]**  |
| TMap< uint8, [FPlayLadderAnimation](/docs/SDK/Source/Classes/structFPlayLadderAnimation.md) > | **[[SyncPlayLadderAnimation]]**  |
| TArray< [FSyncMovementAction](/docs/SDK/Source/Classes/structFSyncMovementAction.md) > | **[[SyncPreMovementActions]]**  |
| TMap< uint8, [FCombatStateReleaseStab](/docs/SDK/Source/Classes/structFCombatStateReleaseStab.md) > | **[[SyncReleaseStab]]**  |
| TMap< uint8, [FSyncSpawnAnimationParams](/docs/SDK/Source/Classes/structFSyncSpawnAnimationParams.md) > | **[[SyncSpawnAnimation]]**  |
| TMap< uint8, [FCombatStateStartAttack](/docs/SDK/Source/Classes/structFCombatStateStartAttack.md) > | **[[SyncStartAttack]]**  |
| TMap< uint8, [FCombatStateFire](/docs/SDK/Source/Classes/structFCombatStateFire.md) > | **[[SyncStartFire]]**  |
| TMap< uint8, [FCombatStateHeavyAttack](/docs/SDK/Source/Classes/structFCombatStateHeavyAttack.md) > | **[[SyncStartHeavyAttack]]**  |
| TMap< uint8, [FSyncStartMovementParams](/docs/SDK/Source/Classes/structFSyncStartMovementParams.md) > | **[[SyncStartMovementParams]]**  |
| TMap< uint8, [FServerTrapEventParams](/docs/SDK/Source/Classes/structFServerTrapEventParams.md) > | **[[SyncTrapEvent]]**  |
| float | **[[TimeBetweenDiscrepancyDetected]]**  |
| bool | **[[bAutorunInitialized]]**  |
| bool | **[[bInitialAutorunExpired]]**  |
| bool | **[[bIsInNoStopAutorun]]**  |
| bool | **[[bLockIntoForcedAutorun]]**  |
| bool | **[[bPendingEndForcedAutorun]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200