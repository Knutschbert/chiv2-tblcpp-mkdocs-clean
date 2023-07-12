---
title: UGameplayRules
type: class
aliases: UGameplayRules
share: false

---

# UGameplayRules





Inherits from UActorComponent

## Public Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[[ApplyDamageConditions]]**(AActor * HitActor, const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & DamageEvent) |
| EAttackerBlockedPolicy | **[[GetAttackerBlockedPolicy]]**(EAttackerBlockedPolicy InAttackerBlockedPolicy, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * AttackingCharacter, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * DefendingCharacter, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * AttackingItem, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * DefendingItem, bool bSameAttackClash) |
| EComboTimingPolicy | **[[GetComboTimingPolicy]]**(EComboTimingPolicy InComboTimingPolicy, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character, FName CombatState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & PrevAttack, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & NextAttack) |
| ECrowdControlVariant | **[[GetCrowdControlVariant]]**(ECrowdControlVariant InCrowdControlVariant, AActor * HitActor, FName CombatState, TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > InventoryItemClass, FName AbilityName, [UAttackType](/docs/SDK/Source/Classes/classUAttackType.md) * AttackType, bool IsOnHorse) |
| EDefenderBlockedPolicy | **[[GetDefenderBlockedPolicy]]**(bool & bShouldDisarm, EDefenderBlockedPolicy InDefenderBlockedPolicy, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * AttackingCharacter, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * DefendingCharacter, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * AttackingItem, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * DefendingItem, bool bProjectileAttack, bool bSameAttackClash, bool bWasBlockedWithParryForgivenessWindow) |
| FVector | **[[GetDisarmImpulse]]**(const [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * AttackerItem, const FVector HitDirection) const |
| [FGoreEvent](/docs/SDK/Source/Classes/structFGoreEvent.md) | **[[GetGoreEventOnDamage]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & DamageTakenEvent, bool bIsRagdollHit, bool bShouldApplyConditions) |
| float | **[[GetRangedInaccuracy]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Projectile) |
| bool | **[[IsBlocking]]**(const [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character, FName AttackName, FName CombatState, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * AttackingCharacter) const |
| bool | **[[IsValidSelfInflictedDamageSource]]**([UDamageSource](/docs/SDK/Source/Classes/classUDamageSource.md) * DamageSource) |
| void | **[[OnDamageTaken]]**(EOnHitEffect & OutHitEffect, ECrowdControlVariant & OutCrowdControlVariant, EOnHitEffect InHitEffect, ECrowdControlVariant InCrowdControlVariant, AActor * HitActor, const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & DamageEvent, FName AttackName, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * AttackingItem, [UAttackType](/docs/SDK/Source/Classes/classUAttackType.md) * AttackType) |
| bool | **[[OnParryBreak]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * AttackingCharacter, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * DefendingCharacter, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * AttackingItem, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * DefendingItem) |
| void | **[[OnProjectileHit]]**(EOnProjectileHitEffect & OutHitEffect, float & OutBounceVelocityModifier, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Projectile, EOnProjectileHitEffect InHitEffect, const FHitResult & InHitResult, float InBounceVelocityModifier) |
| bool | **[[ShouldAttackBeCountered]]**(const [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * HitCharacter, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * AttackingCharacter, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * AttackingItem, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * DefenderItem) const |
| bool | **[[ShouldBlockSameAttack]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * AttackingCharacter, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * DefendingCharacter) const |
| bool | **[[ShouldComboCancelQueue]]**(FName CombatState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & Attack) |
| bool | **[[ShouldGotoDowned]]**(AActor * Target, AActor * Initiator, FName AbilityName, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * InventoryItem, [UDamageSource](/docs/SDK/Source/Classes/classUDamageSource.md) * DamageType, const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & DamageTakenEvent) |
| bool | **[[ShouldPlayDamageTaken]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & DamageTakenEvent) |
| bool | **[[ShouldScoreKill]]**(AController * Killer, AController * Killed, const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & DamageEvent) |
| bool | **[[ShouldStartActiveRiposteWindow]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |
| bool | **[[ShouldStartCounterWindow]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |
| bool | **[[ShouldStartProjectileCounterWindow]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |
| bool | **[[TutorialCanDamage]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * InitiatorCharacter, AActor * TargetActor) |
| | **[[UGameplayRules]]**() |
| float | **[[UpdateAimPenalty]]**(float DeltaSeconds, const TArray< [FAimPenalty](/docs/SDK/Source/Classes/structFAimPenalty.md) > & AimPenalties) |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[AimPenalty]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200