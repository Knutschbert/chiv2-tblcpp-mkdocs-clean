---
title: FParryEventState
type: struct
aliases: FParryEventState
share: false

---

# FParryEventState





## Public Functions

|                | Name           |
| -------------- | -------------- |
| TBL_API | **[[FParryEventState]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| FName | **[[AttackerAttackName]]**  |
| EAttackerBlockedPolicy | **[[AttackerBlockedPolicy]]**  |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[AttackerInventoryItem]]**  |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[AttackerInventoryItemClass]]**  |
| FName | **[[AttackerPostCombatState]]**  |
| FName | **[[DefenderAttackName]]**  |
| EDefenderBlockedPolicy | **[[DefenderBlockedPolicy]]**  |
| ECrowdControlVariant | **[[DefenderCrowdControlVariant]]**  |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[DefenderInventoryItem]]**  |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[DefenderInventoryItemClass]]**  |
| FName | **[[DefenderPostCombatState]]**  |
| FVector | **[[HitDirection]]**  |
| FVector | **[[HitLocation]]**  |
| FVector | **[[ImpactPoint]]**  |
| int32 | **[[ParryAttackID]]**  |
| uint8 | **[[bDefenderDisarmed]]**  |
| uint8 | **[[bIsAltAttack]]**  |
| uint8 | **[[bIsCounterSuccess]]**  |
| uint8 | **[[bProjectileAttack]]**  |
| uint8 | **[[bSameAttackClash]]**  |
| uint8 | **[[bTakeDamage]]**  |
| uint8 | **[[bWasBlockedWithParryForgivenessWindow]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:01 +0200