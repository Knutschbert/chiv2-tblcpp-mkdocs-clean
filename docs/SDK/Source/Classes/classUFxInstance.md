---
title: UFxInstance
type: class
aliases: UFxInstance
share: false

---

# UFxInstance





Inherits from [UFxEventListener](/docs/SDK/Source/Classes/classUFxEventListener.md), [IInstancedObjectContainer](/docs/SDK/Source/Classes/classIInstancedObjectContainer.md), [UTBLObject](/docs/SDK/Source/Classes/classUTBLObject.md), [UAssemblyObject](/docs/SDK/Source/Classes/classUAssemblyObject.md), UObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[Cleanup]]**() |
| void | **[[OnActorPreAbilityInitiate]]**() |
| void | **[[OnCombatStateChangedInternal]]**(AActor * InActor, FName EventName, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo) |
| void | **[[OnKilledInternal]]**(const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & DamageEvent) |
| void | **[[PlayCharacterCombatStateSound]]**(const AActor * SoundActor, const FName PreviousCombatState, const FName NewCombatState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) AttackInfo, const [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * CombatState) |
| void | **[[PlayWeaponCombatStateSound]]**(const AActor * SoundActor, const FName PreviousCombatState, const FName NewCombatState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) AttackInfo, const [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * CombatState) |
| | **[[UFxInstance]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[[AreBloodDecalsRestricted]]**() const |
| void | **[[BP_ResetPostProcess]]**() |
| UMaterialInstanceDynamic * | **[[GetCharacterPostProcessMID]]**() const |
| void | **[[ResetCharacterPostProcessMID]]**() |
| void | **[[SetCharacterPostProcessMID]]**(UMaterialInstanceDynamic * InCharacterPostProcessMID) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| AActor * | **[[Actor]]**  |
| UAkAudioEvent * | **[[BandageAppliedSound]]**  |
| EDelegateRemovalPolicy | **[[DelegateRemovalPolicy]]**  |
| TArray< [UFxEventListener](/docs/SDK/Source/Classes/classUFxEventListener.md) * > | **[[EventListeners]]**  |
| int32 | **[[Flags]]**  |
| float | **[[PlayBandageDelay]]**  |
| float | **[[PlaySuicideDelay]]**  |
| EStopTimerPolicy | **[[StopTimerPolicy]]**  |
| bool | **[[bUnbindOnAttackEnd]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200