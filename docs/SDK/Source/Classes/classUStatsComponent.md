---
title: UStatsComponent
type: class
aliases: UStatsComponent
share: false

---

# UStatsComponent





Inherits from [UTBLComponent](/docs/SDK/Source/Classes/classUTBLComponent.md), [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md), UActorComponent

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AddStamina]]**(float Amount) |
| void | **[[ApplyBonus]]**(EStat Stat, float Value, bool bCanOverCharge) |
| void | **[[ApplyBonusPercent]]**(EStat Stat, float Value, bool bCanOverCharge) |
| void | **[[ApplyModDelta]]**(TEnumAsByte< EMod::Type > Mod, int32 Delta) |
| bool | **[[ApplyPlayerCountHealthScalingCurve]]**(UObject * Target, UCurveFloat * OverrideCurve) |
| float | **[[Bonus]]**(EStat Stat) const |
| float | **[[BonusPercent]]**(EStat Stat) const |
| void | **[[BroadcastDamageTaken]]**([FDamageTakenEventCompressed](/docs/SDK/Source/Classes/structFDamageTakenEventCompressed.md) Event, int32 InvocationId) |
| void | **[[BroadcastHealOverTime]]**(float Amount, float Speed, UCurveFloat * Curve, [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * InstigatorPlayerState, bool bOverheal, EHealingSource HealingSource) |
| void | **[[BroadcastKilled]]**(const TArray< AActor * > & Killers, [FBroadcastKilledParams](/docs/SDK/Source/Classes/structFBroadcastKilledParams.md) Params) |
| float | **[[Current]]**(EStat Stat) const |
| int32 | **[[DisableRegeneration]]**(EStat Stat) |
| void | **[[DrainStamina]]**(float Amount) |
| EFaction | **[[GetAllowedDamagingFaction]]**() |
| int32 | **[[GetExperienceLevel]]**() |
| float | **[[GetHealOverTimeLeft]]**() const |
| float | **[[GetHealthPercent]]**() const |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| [FStatEntry](/docs/SDK/Source/Classes/structFStatEntry.md) | **[[GetStat]]**(EStat Stat) const |
| [UStatsDelegateObject](/docs/SDK/Source/Classes/classUStatsDelegateObject.md) * | **[[GetStatChangedDelegate]]**(EStat Stat) |
| bool | **[[HasHealOverTime]]**() const |
| bool | **[[HasHealOverTimeOfSource]]**(EHealingSource HealingSource) const |
| bool | **[[HasMod]]**(TEnumAsByte< EMod::Type > Mod) const |
| bool | **[[IsDead]]**() const |
| bool | **[[IsRegenerationDisabled]]**(EStat Stat) |
| bool | **[[IsValidDamagingFaction]]**(EFaction inDamageFaction) |
| void | **[[OnRep_Health]]**() |
| void | **[[OnRep_MaxHealth]]**() |
| void | **[[OnRep_Stamina]]**() |
| void | **[[ReceiveExperienceChanged]]**(float Amount, [UDamageSource](/docs/SDK/Source/Classes/classUDamageSource.md) * DamageSource, AActor * InitiatorActor) |
| void | **[[ReceiveHealthChanged]]**(float Amount, [UDamageSource](/docs/SDK/Source/Classes/classUDamageSource.md) * DamageSource, AActor * InitiatorActor) |
| void | **[[ServerDebugApplyBonus]]**(EStat Stat, float Value) |
| void | **[[ServerDebugApplyDamage]]**(float Damage, [UDamageSource](/docs/SDK/Source/Classes/classUDamageSource.md) * DamageSource) |
| void | **[[ServerDebugSetBase]]**(EStat Stat, float Value) |
| void | **[[SetAllowedDamagingFaction]]**(EFaction InFaction) |
| void | **[[SetBase]]**(EStat Stat, float Value, bool bCanOverCharge) |
| void | **[[StartHealOverTime]]**(float Amount, float Speed, UCurveFloat * Curve, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Healer, [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * InstigatorPlayerState, bool AwardHealingScore, bool bOverheal, EHealingSource HealingSource) |
| | **[[UStatsComponent]]**() |
| void | **[[UndoDisableRegeneration]]**(int32 ID) |
| float | **[[base]]**(EStat Stat) const |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< [UDamageSource](/docs/SDK/Source/Classes/classUDamageSource.md) * > | **[[AllowedDamageSource]]**  |
| TArray< [FBaseStatEntry](/docs/SDK/Source/Classes/structFBaseStatEntry.md) > | **[[BaseStats]]**  |
| [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) | **[[LastDamageEvent]]**  |
| float | **[[LastParrySuccessTime]]**  |
| [FReplicatedArray_FModEntry](/docs/SDK/Source/Classes/structFReplicatedArray__FModEntry.md) | **[[Mods]]**  |
| EConditionType | **[[OnDamageApplyCondition]]**  |
| FDamageTakenSignature | **[[OnDamageCaused]]**  |
| FDamageFailedSignature | **[[OnDamageFailed]]**  |
| FDamageTakenSignature | **[[OnDamageTaken]]**  |
| FExperienceLevelChangedSignature | **[[OnExperienceLevelChanged]]**  |
| FOnHealOverTime | **[[OnHealOverTimeAdded]]**  |
| FOnHealOverTimeEnded | **[[OnHealOverTimeEnd]]**  |
| FOnHealOverTime | **[[OnHealOverTimeStart]]**  |
| FKilledSignature | **[[OnKilled]]**  |
| FOnNeedsHealingChanged | **[[OnNeedsHealingChanged]]**  |
| FPostDamageTakenSignature | **[[OnPostDamageTaken]]**  |
| FPreBroadcastDamageSignature | **[[OnPreBroadcastDamage]]**  |
| FDamageTakenSignature | **[[OnPreDamageTaken]]**  |
| FScoredKillSignature | **[[OnScoredKill]]**  |
| FOnStaminaDrained | **[[OnStaminaDrained]]**  |
| FStatsChangedSignature | **[[OnStatChanged]]**  |
| FStatHealthChangedSignature | **[[OnStatHealthChanged]]**  |
| FStatsComponentInitialized | **[[OnStatsComponentInitialized]]**  |
| ETeamDamageOptions | **[[OnTeamDamage]]**  |
| UCurveFloat * | **[[PlayerCountHealthScalingCurve]]**  |
| float | **[[PreviousStaminaReduction]]**  |
| [FReplicated_Float](/docs/SDK/Source/Classes/structFReplicated__Float.md) | **[[ReplicatedHealth]]**  |
| [FReplicated_Float](/docs/SDK/Source/Classes/structFReplicated__Float.md) | **[[ReplicatedMaxHealth]]**  |
| [FReplicated_Float](/docs/SDK/Source/Classes/structFReplicated__Float.md) | **[[ReplicatedStamina]]**  |
| TArray< [UStatsDelegateObject](/docs/SDK/Source/Classes/classUStatsDelegateObject.md) * > | **[[StatChangedDelegates]]**  |
| TArray< [FStatRegeneration](/docs/SDK/Source/Classes/structFStatRegeneration.md) > | **[[StatRegeneration]]**  |
| [FStatsArray](/docs/SDK/Source/Classes/structFStatsArray.md) | **[[Stats]]**  |
| UDataTable * | **[[StatsDataTable]]**  |
| FName | **[[StatsDataTableRowName]]**  |
| bool | **[[bAppliedPlayerCountHealthScaling]]**  |
| bool | **[[bDebugGotoDowned]]**  |
| bool | **[[bDisableProjectileDamage]]**  |
| bool | **[[bDisableRegenTimer]]**  |
| bool | **[[bEnableSiegeDamage]]**  |
| bool | **[[bReplicateStats]]**  |
| bool | **[[bStatsScaleToPlayerCount]]**  |
| bool | **[[bStopProjectileOnBlockingHit]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200