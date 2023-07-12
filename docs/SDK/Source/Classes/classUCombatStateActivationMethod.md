---
title: UCombatStateActivationMethod
type: class
aliases: UCombatStateActivationMethod
share: false

---

# UCombatStateActivationMethod





Inherits from [UAbilityActivationMethod](/docs/SDK/Source/Classes/classUAbilityActivationMethod.md), [UTBLObject](/docs/SDK/Source/Classes/classUTBLObject.md), [UAssemblyObject](/docs/SDK/Source/Classes/classUAssemblyObject.md), UObject

Inherited by [UChargingActivationMethod](/docs/SDK/Source/Classes/classUChargingActivationMethod.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[UCombatStateActivationMethod]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[OnCombatStateChanged]]**(AActor * Actor, FName PreviousState, FName NewState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * InCombatState) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| FName | **[[AbilitiesTableRow]]**  |
| FName | **[[CostExceededGotoState]]**  |
| TArray< FName > | **[[CostExceededInterruptableStates]]**  |
| int32 | **[[EmoteId]]**  |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[InventoryItem]]**  |
| FName | **[[KeyBind]]**  |
| bool | **[[bCombatStateAttackStarted]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| bool | **[[bAnimationDataTableNotFound]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200