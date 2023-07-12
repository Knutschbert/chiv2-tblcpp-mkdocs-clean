---
title: FParryEventReplicated
type: struct
aliases: FParryEventReplicated
share: false

---

# FParryEventReplicated





## Public Functions

|                | Name           |
| -------------- | -------------- |
| TBL_API | **[[FParryEventReplicated]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| uint8 | **[[AttackerAttackIndex]]**  |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[AttackerInventoryItem]]**  |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[AttackerInventoryItemClass]]**  |
| uint8 | **[[AttackerPostCombatStateIndex]]**  |
| uint8 | **[[DefenderAttackIndex]]**  |
| ECrowdControlVariant | **[[DefenderCrowdControlVariant]]**  |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[DefenderInventoryItemClass]]**  |
| uint8 | **[[DefenderPostCombatStateIndex]]**  |
| FVector_NetQuantizeNormal | **[[HitDirection]]**  |
| FVector_NetQuantize | **[[HitLocation]]**  |
| FVector_NetQuantize | **[[ImpactPoint]]**  |
| int32 | **[[ParryAttackID]]**  |
| uint8 | **[[bDefenderDisarmed]]**  |
| uint8 | **[[bIsAltAttack]]**  |
| uint8 | **[[bIsCounterSuccess]]**  |
| uint8 | **[[bProjectileAttack]]**  |
| uint8 | **[[bSameAttackClash]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:01 +0200