---
title: UCombatStateComponent
type: class
aliases: UCombatStateComponent
share: false

---

# UCombatStateComponent





Inherits from UActorComponent, [IInstancedObjectContainer](/docs/SDK/Source/Classes/classIInstancedObjectContainer.md), [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AnimNotify_ActivateAbility]]**() |
| void | **[[AnimNotify_EndWeaponTracers]]**() |
| void | **[[BroadcastCrowdControl_NoDamage]]**(ECrowdControlCombatState CombatState, [FCrowdControlParams](/docs/SDK/Source/Classes/structFCrowdControlParams.md) CrowdControlParams, bool bSkipAutonomous) |
| void | **[[BroadcastGetUp]]**(FName Direction) |
| bool | **[[CanCrouch]]**() const |
| bool | **[[CanDoHeavyAttack]]**() |
| void | **[[ClientCancelProjectile]]**(FName CombatState) |
| void | **[[ClientRecordPreviousSwingThroughInfo]]**([FSwingThroughInfo](/docs/SDK/Source/Classes/structFSwingThroughInfo.md) SwingThroughInfo) |
| void | **[[CrowdControl_NoDamage]]**(ECrowdControlCombatState CombatState, [FCrowdControlParams](/docs/SDK/Source/Classes/structFCrowdControlParams.md) CrowdControlParams, bool bAutonomous) |
| void | **[[DebugGotoState]]**(FName CombatState, FName HitDirection, int32 CrowdControlVariant) |
| bool | **[[DidLastAttackDisarm]]**() const |
| void | **[[ExtendCounterWindow]]**() |
| float | **[[GetAttackCooldownRemainingByName]]**(FName AttackName) |
| FString | **[[GetAttackTransitionString]]**(EAttackTransition AttackTransition) const |
| float | **[[GetClientTimeStamp]]**() const |
| [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * | **[[GetCombatStateBlueprint]]**(const FName & StateName) |
| [UCombatStateQueue](/docs/SDK/Source/Classes/classUCombatStateQueue.md) * | **[[GetCombatStateQueue]]**() const |
| [UCombatStateSynchronization](/docs/SDK/Source/Classes/classUCombatStateSynchronization.md) * | **[[GetCombatStateSynchronization]]**() const |
| FString | **[[GetComboTimingPolicyString]]**(EComboTimingPolicy ComboTimingPolicy) const |
| float | **[[GetCurrentAnimationLength]]**() const |
| FName | **[[GetCurrentAttack]]**() const |
| FName | **[[GetCurrentAttackCategory]]**() const |
| FName | **[[GetCurrentAttackComboState]]**() const |
| FName | **[[GetCurrentAttackDirection]]**() const |
| [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) | **[[GetCurrentAttackInfo]]**(bool bLastValidAttack) const |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[GetCurrentAttackItem]]**() const |
| float | **[[GetCurrentAttackTime]]**() const |
| EAttackTypeCategory | **[[GetCurrentAttackTypeCategory]]**() const |
| [FCombatStateInfo](/docs/SDK/Source/Classes/structFCombatStateInfo.md) | **[[GetCurrentStateInfo]]**() const |
| float | **[[GetFeintMinTime]]**() const |
| FName | **[[GetLastHitDirection]]**() const |
| ECrowdControlDirection | **[[GetLastHitDirection_CrowdControl]]**() const |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| float | **[[GetMinimumHoldingTime]]**() const |
| [FCombatStateInfo](/docs/SDK/Source/Classes/structFCombatStateInfo.md) | **[[GetPreviousStateInfo]]**(bool bLastAttackState, bool bIgnoreQuickIdle) const |
| [FCombatStateInfo](/docs/SDK/Source/Classes/structFCombatStateInfo.md) | **[[GetPreviousStateInfoByName]]**(FName InCombatState) const |
| FName | **[[GetQueuedInput]]**() const |
| FName | **[[GetState]]**() const |
| float | **[[GetTimeInCurrentState]]**() |
| void | **[[GotoCounterReadyStateReplicated]]**(int32 ParryAttackID, FName AttackerAttackName) |
| void | **[[GotoParrySuccessReplicated]]**(int32 ParryAttackID, bool bWasBlockedWithParryForgivenessWindow) |
| void | **[[GotoState]]**(FName NextStateName, float OverrideStateTime, bool bStartAttack, ECrowdControlVariant Variant) |
| void | **[[GotoStateReplicated]]**(FName NextStateName, bool bAutonomous, float OverrideStateTime, ECrowdControlVariant Variant) |
| bool | **[[IsAbilityUnblockable]]**() const |
| bool | **[[IsActiveCounter]]**() const |
| bool | **[[IsActiveRiposte]]**() const |
| bool | **[[IsCancelling]]**() const |
| bool | **[[IsCombo]]**() const |
| bool | **[[IsCounter]]**() const |
| bool | **[[IsDowned]]**() const |
| bool | **[[IsFeint]]**() const |
| bool | **[[IsFocused]]**() const |
| bool | **[[IsHeavy]]**() const |
| bool | **[[IsHoldAttackPressed]]**() const |
| bool | **[[IsHoldingInput]]**() const |
| bool | **[[IsInActiveRiposteWindow]]**() const |
| bool | **[[IsInCounterWindow]]**() const |
| bool | **[[IsInParryForgivenessWindow]]**() |
| bool | **[[IsInProjectileCounterWindow]]**() const |
| bool | **[[IsInState]]**(FName StateName) const |
| bool | **[[IsInterrupted]]**() const |
| bool | **[[IsKnockedDown]]**() const |
| bool | **[[IsParryQueued]]**() const |
| bool | **[[IsPreMovement]]**() const |
| bool | **[[IsRiposte]]**() const |
| bool | **[[IsUsingAttackTracers]]**() const |
| void | **[[OnAbilityInitiated]]**([AAbilityInvocation](/docs/SDK/Source/Classes/classAAbilityInvocation.md) * Invocation) |
| void | **[[OnActorHit]]**(AActor * SelfActor, AActor * OtherActor, FVector NormalImpulse, const FHitResult & Hit) |
| void | **[[OnClash]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Initiator, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Target) |
| void | **[[OnDamage]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & DamageEvent) |
| void | **[[OnDamageCaused]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & DamageEvent) |
| void | **[[OnDismount]]**(AActor * AttachParent, EDismountType DismountType) |
| void | **[[OnEndAnimation]]**() |
| void | **[[OnEndAnimationTimeout]]**(float OverTime) |
| void | **[[OnHitWorld]]**(AActor * HitActor, bool bBreakableHit, bool bAutonomous) |
| void | **[[OnItemStackChanged]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item, int32 Delta) |
| void | **[[OnKilled]]**() |
| void | **[[OnMeleeSuccess]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * HitCharacter) |
| void | **[[OnParrySuccess]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * DefendingCharacter, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * AttackingCharacter, [FParryEventState](/docs/SDK/Source/Classes/structFParryEventState.md) ParryEventState) |
| void | **[[OnRagdolled]]**() |
| void | **[[OnReplicatedCombatState]]**() |
| void | **[[OnStaminaDrained]]**() |
| void | **[[OnWasParried]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * AttackingCharacter, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * DefendingCharacter, [FParryEventState](/docs/SDK/Source/Classes/structFParryEventState.md) ParryEventState) |
| void | **[[QueueHeldInputs]]**(FName InputName, bool bIgnoreLastAttackInput) |
| void | **[[Reload]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item, bool bReplicateToClient) |
| [FReplicatedCombatStateInfo](/docs/SDK/Source/Classes/structFReplicatedCombatStateInfo.md) | **[[ReplicateCombatState]]**(bool bForceNetUpdate) |
| void | **[[ResetQueuedInputs]]**() |
| void | **[[ServerManualReload]]**([FManualReload](/docs/SDK/Source/Classes/structFManualReload.md) Params) |
| void | **[[SetSimulatedCombatState]]**(bool bBroadcastEndState) |
| | **[[UCombatStateComponent]]**() |
| bool | **[[WasBlockedWithParryForgivenessWindow]]**() const |
| bool | **[[WasHitByProjectile]]**() const |
| bool | **[[WasInterruptedByJab]]**() const |
| bool | **[[WasLastHitTeamHit]]**() const |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [FSwingThroughInfo](/docs/SDK/Source/Classes/structFSwingThroughInfo.md) | **[[CurrentSwingThroughInfo]]**  |
| TArray< [FDelayedQueueHeldInputs](/docs/SDK/Source/Classes/structFDelayedQueueHeldInputs.md) > | **[[DelayedQueueHeldInputs]]**  |
| FString | **[[DisplayDebugTitle]]**  |
| FName | **[[InitialState]]**  |
| FOnActiveRiposteWindow | **[[OnActiveRiposteWindowEnd]]**  |
| FOnActiveRiposteWindow | **[[OnActiveRiposteWindowStart]]**  |
| FCombatStateChanged | **[[OnAnimationEnd]]**  |
| FCombatStateBegin | **[[OnCombatStateBegin]]**  |
| FCombatStateChanged | **[[OnCombatStateChanged]]**  |
| FCombatStateEnd | **[[OnCombatStateEnd]]**  |
| FCombatStateEvent | **[[OnCombatStateEvent]]**  |
| FOnCounterWindow | **[[OnCounterWindowEnd]]**  |
| FOnCounterWindow | **[[OnCounterWindowStart]]**  |
| FCrowdControlNoDamage | **[[OnCrowdControlNoDamage]]**  |
| FOnDownedStateChanged | **[[OnDownedStateChanged]]**  |
| FOnGetUp | **[[OnGetUp]]**  |
| FOnCounterWindow | **[[OnProjectileCounterWindowEnd]]**  |
| FOnCounterWindow | **[[OnProjectileCounterWindowStart]]**  |
| FRagdollHitEvent | **[[OnRagdollHitEvent]]**  |
| FRagdollHitFxEvent | **[[OnRagdollHitFxEvent]]**  |
| FStartAttackEvent | **[[OnStartAttack]]**  |
| FStartAttackEvent | **[[OnSwitchAttack]]**  |
| int32 | **[[OverrideCrowdControlVariant]]**  |
| FName | **[[OverrideHitDirection]]**  |
| float | **[[OverrideHitDirectionTime]]**  |
| FPostUpdateWeaponTracers | **[[PostUpdateWeaponTracers]]**  |
| [FReplicatedCombatStateInfo](/docs/SDK/Source/Classes/structFReplicatedCombatStateInfo.md) | **[[SimulatedCombatState]]**  |
| [FTurnLimitState](/docs/SDK/Source/Classes/structFTurnLimitState.md) | **[[TurnLimitState]]**  |
| uint8 | **[[bForceCanMount]]**  |
| uint8 | **[[bHorseAttackSwitchDirection]]**  |
| uint8 | **[[bWeaponTracersUpdating]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [UCombatStateQueue](/docs/SDK/Source/Classes/classUCombatStateQueue.md) * | **[[CombatStateQueue]]**  |
| [UCombatStateSynchronization](/docs/SDK/Source/Classes/classUCombatStateSynchronization.md) * | **[[CombatStateSynchronization]]**  |
| UDataTable * | **[[NonAbilitiesAnimationDataTable]]**  |
| [FReplicated_FReplicatedCombatStateInfo](/docs/SDK/Source/Classes/structFReplicated__FReplicatedCombatStateInfo.md) | **[[ReplicatedCombatState]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200