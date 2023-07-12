---
title: UAttackType
type: class
aliases: UAttackType
share: false

---

# UAttackType





Inherits from [UAssemblyBlueprint](/docs/SDK/Source/Classes/classUAssemblyBlueprint.md), UBlueprint

## Public Functions

|                | Name           |
| -------------- | -------------- |
| EOnHitEffect | **[[GetHitEffect]]**(AActor * Target) |
| | **[[UAttackType]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| EActivateAbility | **[[ActivateAbility]]**  |
| FName | **[[ActivateCombatState]]**  |
| EAnimationType | **[[AnimationType]]**  |
| FName | **[[AttackCategory]]**  |
| EAttackTypeCategory | **[[AttackTypeCategory]]**  |
| EAttackerBlockedPolicy | **[[AttackerBlockedPolicy]]**  |
| EAttackerBlockedPolicy | **[[AttackerCounteredPolicy]]**  |
| TMap< EBlockingCategory, EAttackerBlockedPolicy > | **[[BlockedPolicyPerCategory]]**  |
| EWorldHitPolicy | **[[BreakableHitPolicy]]**  |
| TArray< FName > | **[[CanBeBlockedByParryBox]]**  |
| UCurveFloat * | **[[ChargeStabDamageModifier]]**  |
| EClashPolicy | **[[ClashPolicy]]**  |
| ECombatStateBehavior | **[[CombatStateBehavior]]**  |
| TMap< FName, [FCombatStateSlowdown](/docs/SDK/Source/Classes/structFCombatStateSlowdown.md) > | **[[CombatStateSlowdown]]**  |
| EComboTimingPolicy | **[[ComboFromJabPolicy]]**  |
| EComboTimingPolicy | **[[ComboFromParryReleasePolicy]]**  |
| EComboTimingPolicy | **[[ComboFromRecoveryPolicy]]**  |
| EComboTimingPolicy | **[[ComboFromReleasePolicy]]**  |
| EComboTimingPolicy | **[[ComboFromThwackPolicy]]**  |
| UCurveVector * | **[[DamageScaleAgainstMountedRiders]]**  |
| UCurveVector * | **[[DamageScaleAgainstMounts]]**  |
| UCurveVector * | **[[DamageScaleOnHorseback]]**  |
| EDefenderBlockedPolicy | **[[DefenderBlockedPolicy]]**  |
| FText | **[[Description]]**  |
| float | **[[DownedDamageModifier]]**  |
| float | **[[EarlyHitDelay]]**  |
| [FEarlyHitParams](/docs/SDK/Source/Classes/structFEarlyHitParams.md) | **[[EarlyHitParams]]**  |
| EEarlyHitPolicy | **[[EarlyHitPolicy]]**  |
| TArray< [FFullBodyAnimationModifier](/docs/SDK/Source/Classes/structFFullBodyAnimationModifier.md) > | **[[FullBodyAnimationModifiers]]**  |
| float | **[[FullBodyStartOfReleaseTime]]**  |
| EHeldBehavior | **[[HeldBehavior]]**  |
| float | **[[LockTurnAngle]]**  |
| float | **[[MinimumHoldingTime]]**  |
| EOnHitPolicy | **[[OnHitPolicy]]**  |
| EOnStaminaDrainedPolicy | **[[OnStaminaDrainedPolicy]]**  |
| EDefenderBlockedPolicy | **[[ParrySuccessShieldBreakPolicy]]**  |
| EPassiveShieldPolicy | **[[PassiveShieldPolicy]]**  |
| EReleaseCancelPolicy | **[[ReleaseCancelPolicy]]**  |
| [FStaminaDrain](/docs/SDK/Source/Classes/structFStaminaDrain.md) | **[[StaminaDrain]]**  |
| ECombatStateEvent | **[[StartTurnLock]]**  |
| EOnHitEffect | **[[TargetHitEffect]]**  |
| EOnHitEffect | **[[TargetHitEffectHorse]]**  |
| ETeamHitDamagePolicy | **[[TeamHitDamagePolicy]]**  |
| ETeamHitPolicy | **[[TeamHitPolicy]]**  |
| [FTurnLockParams](/docs/SDK/Source/Classes/structFTurnLockParams.md) | **[[TurnLockParams]]**  |
| int32 | **[[Version]]**  |
| EWindupInputReleasedPolicy | **[[WindupInputReleasedPolicy]]**  |
| EWorldHitPolicy | **[[WorldHitPolicy]]**  |
| bool | **[[bAddComboFromBlockedTime]]**  |
| bool | **[[bAddComboFromMissedAttackTime]]**  |
| bool | **[[bCanAlwaysQueueCombo]]**  |
| bool | **[[bCanBeCancelled]]**  |
| bool | **[[bCanBendUpperBody]]**  |
| bool | **[[bCanCancelOtherAttack]]**  |
| bool | **[[bCanClash]]**  |
| bool | **[[bCanComboInInterrupt]]**  |
| bool | **[[bCanComboInto]]**  |
| bool | **[[bCanComboIntoSelf]]**  |
| bool | **[[bCanComboOutOf]]**  |
| bool | **[[bCanComboOutOfIfMissed]]**  |
| bool | **[[bCanCrouch]]**  |
| bool | **[[bCanFeint]]**  |
| bool | **[[bCanFeintInto]]**  |
| bool | **[[bCanHoldCombo]]**  |
| bool | **[[bCanQueueAttack]]**  |
| bool | **[[bCanRiposte]]**  |
| bool | **[[bCancelOnAttackInput]]**  |
| bool | **[[bCancelUsesStamina]]**  |
| bool | **[[bDisableArmCollision]]**  |
| bool | **[[bDoEarlyHits]]**  |
| bool | **[[bHorseLeftSideAltAttack]]**  |
| bool | **[[bIsUninterruptibleInRelease]]**  |
| bool | **[[bShouldLoopRelease]]**  |
| bool | **[[bSlowdownOnFire]]**  |
| bool | **[[bUseAttackTypeModifier]]**  |
| bool | **[[bUseChargeStabDamageModifier]]**  |
| bool | **[[bUseDownedDamageModifier]]**  |
| bool | **[[bUseLocationBasedDamage]]**  |
| bool | **[[bUseLockTurnAngle]]**  |
| bool | **[[bUseParryBreakDamageModifier]]**  |
| bool | **[[bUseProjectileDamageModifiers]]**  |
| bool | **[[bUseStaminaDrain]]**  |
| bool | **[[bUseTracerHitDirection]]**  |
| bool | **[[bUseTurnLock]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200