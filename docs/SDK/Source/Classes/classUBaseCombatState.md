---
title: UBaseCombatState
type: class
aliases: UBaseCombatState
share: false

---

# UBaseCombatState





Inherits from [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md), [UAssemblyInstance](/docs/SDK/Source/Classes/classUAssemblyInstance.md), UObject

Inherited by [UNativeCombatState_Release](/docs/SDK/Source/Classes/classUNativeCombatState__Release.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AddReloadHint]]**() |
| bool | **[[DidHitInRelease]]**() const |
| void | **[[DropHeavyObject]]**() |
| float | **[[GetStaminaPercent]]**() const |
| bool | **[[NeedToReload]]**() const |
| void | **[[Reload]]**() |
| void | **[[RemoveReloadHint]]**() |
| void | **[[ToggleReloadHint]]**(bool Enable) |
| | **[[UBaseCombatState]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| uint8 | **[[CanReloadInState]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TWeakObjectPtr< UUserWidget > | **[[InputHintsWidget]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200