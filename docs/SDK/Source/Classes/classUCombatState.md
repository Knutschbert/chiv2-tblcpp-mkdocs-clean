---
title: UCombatState
type: class
aliases: UCombatState
share: false

---

# UCombatState





Inherits from [UAssemblyInstance](/docs/SDK/Source/Classes/classUAssemblyInstance.md), UObject

Inherited by [UBaseCombatState](/docs/SDK/Source/Classes/classUBaseCombatState.md), [UHorseMovementState](/docs/SDK/Source/Classes/classUHorseMovementState.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AddTimerHandle]]**(int32 Handle, FName CombatStateName) |
| bool | **[[AutomaticReload]]**() const |
| bool | **[[CanBeCancelled]]**(bool bIsCancelIntoParry) const |
| bool | **[[CanComboFromState]]**() const |
| bool | **[[CanCrouch]]**() const |
| bool | **[[CanDash]]**() const |
| bool | **[[CanFeint]]**() const |
| bool | **[[CanInitiateCrouch]]**() const |
| bool | **[[CanInitiateQueuedAttack]]**() const |
| bool | **[[CanJump]]**() const |
| bool | **[[CanMountActors]]**() const |
| bool | **[[CanSprint]]**() const |
| bool | **[[CanSwitchInventoryItems]]**() const |
| bool | **[[CanUseWeaponsAndSiegeActors]]**() const |
| void | **[[CancelAttack]]**() |
| bool | **[[CannotMove]]**() const |
| bool | **[[CannotUseInteractables]]**() const |
| void | **[[CombatStateEvent]]**(FName EventName) |
| bool | **[[DisableSprintTurn]]**() const |
| float | **[[GetAbilityPropertyValue]]**(FName PropertyName) const |
| EAttackTransition | **[[GetAttackTransition]]**() const |
| FName | **[[GetCancelledCombatState]]**() const |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[GetCharacter]]**() const |
| [UTBLCharacterMovement](/docs/SDK/Source/Classes/classUTBLCharacterMovement.md) * | **[[GetCharacterMovement]]**() const |
| void | **[[GetCharactersCurrentEmote]]**(bool & IsRootAnimation, [FPersonalityEmoteTableRow](/docs/SDK/Source/Classes/structFPersonalityEmoteTableRow.md) & Emote, int32 & EmoteId) const |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[GetCharactersEquippedWeapon]]**() const |
| FName | **[[GetCombatStateFromQueuedAttack]]**() const |
| FName | **[[GetCurrentAttackCategory]]**() const |
| FName | **[[GetCurrentAttackName]]**() const |
| [UAttackType](/docs/SDK/Source/Classes/classUAttackType.md) * | **[[GetCurrentAttackType]]**() const |
| EAttackTypeCategory | **[[GetCurrentAttackTypeCategory]]**() const |
| float | **[[GetDrawStrengthModifier]]**() const |
| float | **[[GetMaxDrawStrengthTime]]**() const |
| float | **[[GetMinimumHoldingTime]]**() const |
| AActor * | **[[GetOwner]]**() const |
| bool | **[[GetQueuedAttackCanComboInInterrupt]]**() const |
| FName | **[[GetQueuedAttackCategory]]**() const |
| FName | **[[GetQueuedAttackName]]**() const |
| [UAttackType](/docs/SDK/Source/Classes/classUAttackType.md) * | **[[GetQueuedAttackType]]**() const |
| EAttackTypeCategory | **[[GetQueuedAttackTypeCategory]]**() const |
| float | **[[GetRemainingTime]]**() const |
| float | **[[GetSoftRecoveryPercent]]**() const |
| float | **[[GetTimeInState]]**() const |
| float | **[[GetTimeInStatePercent]]**() const |
| float | **[[GetTimeSinceLastQueuedAttack]]**() const |
| void | **[[Getup]]**(FName Direction) |
| void | **[[HoldState]]**(EHeldBehavior HeldBehavior) |
| bool | **[[IsAttackQueued]]**() const |
| bool | **[[IsCombatStateTimerActive]]**(int32 Handle) const |
| bool | **[[IsCombo]]**() const |
| bool | **[[IsCounter]]**() const |
| bool | **[[IsFeint]]**() const |
| bool | **[[IsFocusQueued]]**() |
| bool | **[[IsHeavy]]**() const |
| bool | **[[IsHoldAttackPressed]]**() const |
| bool | **[[IsHoldingInput]]**() const |
| bool | **[[IsHoldingReloadableThrowable]]**() const |
| bool | **[[IsInitialized]]**() const |
| bool | **[[IsOutOfAmmo]]**() const |
| bool | **[[IsRiposte]]**() const |
| bool | **[[IsWithinWindow]]**(float WindowTime, bool bFromEndOfState) const |
| void | **[[KnockRiderOffHorse]]**() |
| bool | **[[NeedsReload]]**() const |
| void | **[[OnActivateAbility]]**() |
| void | **[[OnFireProjectile]]**() |
| void | **[[OnFocusPressed]]**() |
| void | **[[OnFocusReleased]]**() |
| void | **[[OnItemStackChanged]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item, int32 Delta) |
| void | **[[OnJumpPressed]]**() |
| void | **[[OnMovementInput]]**(FName Direction) |
| void | **[[OnReloadPressed]]**() |
| void | **[[OnStartEquip]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item) |
| bool | **[[OverrideCrowdControlEvent]]**(ECrowdControlCombatState CombatState, ECrowdControlVariant Variant) |
| void | **[[PlayEquipAnimation]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item) |
| void | **[[ProjectileInterrupted]]**() |
| void | **[[ResetAmmoAttachment]]**() |
| void | **[[ResetMinimumHoldingTime]]**() |
| void | **[[RestOfCurrentState]]**(bool InCanSwitchInventoryItems, bool InCanMountActors) |
| void | **[[Revive]]**() |
| void | **[[SetCombatStateTimer]]**(int32 & OutHandle, FTimerDynamicDelegate Delegate, float Time, bool bLooping) |
| void | **[[SetWeaponLoaded]]**(bool bLoaded) |
| bool | **[[ShouldRemainInSprint]]**() const |
| bool | **[[ShouldSprintDecelerate]]**() const |
| bool | **[[ShouldUseDrawStrengthModifier]]**() const |
| void | **[[StartAttack]]**() |
| void | **[[StartChargeStab]]**() |
| void | **[[StartFeint]]**() |
| void | **[[StartFire]]**() |
| void | **[[StartFocus]]**() |
| void | **[[StartHeavyAttack]]**(bool bIsHeavy) |
| void | **[[StartHoldAttack]]**() |
| void | **[[StartReleaseStab]]**() |
| void | **[[StartRevive]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * DownedCharacter) |
| void | **[[StopFocus]]**() |
| void | **[[SyncDrawStrength]]**() const |
| | **[[UCombatState]]**() |
| void | **[[UseItem]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[ActionClearAttackQueue]]**() |
| void | **[[ActionClearHeldAttackQueue]]**() |
| void | **[[ActionClearToggleAltAttack]]**() |
| void | **[[ActionGotoState]]**(FName NextState, float OverrideStateTime, bool bResetStateTime) |
| void | **[[ActionQueueAttack]]**() |
| void | **[[EventBeginFire]]**(FName AttackName, bool bHeldQueue) |
| void | **[[EventBeginState]]**(FName PreviousState, float PreviousStateTime, float AnimationLength) |
| void | **[[EventCancelAttack]]**() |
| bool | **[[EventCannotQueueAttack]]**([UAttackType](/docs/SDK/Source/Classes/classUAttackType.md) * AttackType) |
| void | **[[EventDamage]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & DamageEvent) |
| void | **[[EventDamageCaused]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & DamageEvent) |
| void | **[[EventEndAnimation]]**() |
| void | **[[EventEndState]]**(FName NextState, bool bStartAttack) |
| void | **[[EventLanded]]**(ACharacter * InTarget) |
| void | **[[EventMeleeSuccess]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * DamagedCharacter) |
| void | **[[EventParrySuccess]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * ParriedCharacter) |
| void | **[[EventRagdolled]]**() |
| void | **[[EventTick]]**(float DeltaSeconds) |
| void | **[[EventWasParried]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * ParryingCharacter) |
| void | **[[HandleDelayedStartAttack]]**() |
| void | **[[OnEndTurnLock]]**() |
| void | **[[OnTurnLockTimeout]]**(float OverTime) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< FName > | **[[AttackTags]]**  |
| int32 | **[[CrowdControlPriority]]**  |
| float | **[[CrowdControlThreshold]]**  |
| float | **[[CurrentAnimationLength]]**  |
| float | **[[DefaultTime]]**  |
| TEnumAsByte< EAbilityTermination::Type > | **[[EndAttackReason]]**  |
| EKillReason | **[[KillReason]]**  |
| FRotator | **[[KnockRiderOffHorseRotation]]**  |
| float | **[[MinimumHoldingTime]]**  |
| [FCombatStateModifiers](/docs/SDK/Source/Classes/structFCombatStateModifiers.md) | **[[ModifierList]]**  |
| TArray< TEnumAsByte< EMod::Type > > | **[[Modifiers]]**  |
| int32 | **[[PushingPriority]]**  |
| [FScaleDirectionParams](/docs/SDK/Source/Classes/structFScaleDirectionParams.md) | **[[ScaleDirectionalMovement]]**  |
| float | **[[StartTime]]**  |
| FName | **[[StateName]]**  |
| [FTurnLimitParams](/docs/SDK/Source/Classes/structFTurnLimitParams.md) | **[[TurnLimit]]**  |
| [FTurnLockParams](/docs/SDK/Source/Classes/structFTurnLockParams.md) | **[[TurnLock]]**  |
| int32 | **[[Version]]**  |
| uint8 | **[[bAnimationEnded]]**  |
| uint8 | **[[bCanBeRestarted]]**  |
| uint8 | **[[bCanMountActors]]**  |
| uint8 | **[[bCanSwitchInventoryItems]]**  |
| uint8 | **[[bCancelHorseAttack]]**  |
| uint8 | **[[bEndSpawnSpeedBonus]]**  |
| uint8 | **[[bEndWeaponTracers]]**  |
| uint8 | **[[bIsAttackState]]**  |
| uint8 | **[[bIsClimbingState]]**  |
| uint8 | **[[bIsSprintState]]**  |
| uint8 | **[[bKnockRiderOffHorse]]**  |
| uint8 | **[[bRemainInSprint]]**  |
| uint8 | **[[bSameAttackClash]]**  |
| bool | **[[bSoftRecovery]]**  |
| uint8 | **[[bSprintDecelerate]]**  |
| uint8 | **[[bUseScaleDirectionalMovement]]**  |
| uint8 | **[[bUseTurnLock]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| EAttackTransition | **[[AttackTransition]]**  |
| TArray< [FNextStateTimer](/docs/SDK/Source/Classes/structFNextStateTimer.md) > | **[[NextStateTimers]]**  |
| int32 | **[[PushingId]]**  |
| int32 | **[[ScaleDirectionId]]**  |
| int32 | **[[SlowdownId]]**  |
| [FCombatStateSlowdown](/docs/SDK/Source/Classes/structFCombatStateSlowdown.md) | **[[SlowdownState]]**  |
| TArray< int32 > | **[[TimerHandles]]**  |
| [FTurnLockState](/docs/SDK/Source/Classes/structFTurnLockState.md) | **[[TurnLockState]]**  |
| uint8 | **[[bBeginFire]]**  |
| uint8 | **[[bCanInitiateCrouch]]**  |
| uint8 | **[[bDidStartAttack]]**  |
| uint8 | **[[bIsActive]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200