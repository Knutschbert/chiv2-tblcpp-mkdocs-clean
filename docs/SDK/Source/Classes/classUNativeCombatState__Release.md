---
title: UNativeCombatState_Release
type: class
aliases: UNativeCombatState_Release
share: false

---

# UNativeCombatState_Release





Inherits from [UBaseCombatState](/docs/SDK/Source/Classes/classUBaseCombatState.md), [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md), [UAssemblyInstance](/docs/SDK/Source/Classes/classUAssemblyInstance.md), UObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[[AllowSprinting]]**() const |
| void | **[[HandleQueuedParryCounter]]**() |
| void | **[[OnAllowCounters]]**(float OverTime) |
| void | **[[ShouldDelayCounter]]**(bool & Delay, float & DelayTime) |
| | **[[UNativeCombatState_Release]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| uint8 | **[[AllowCounters]]**  |
| float | **[[ClearAttackQueueTime]]**  |
| [UAttackType](/docs/SDK/Source/Classes/classUAttackType.md) * | **[[DashJumpAttackType]]**  |
| TMap< FName, float > | **[[DelayCounterTime]]**  |
| float | **[[DelayCounterTimeOnBlocked]]**  |
| float | **[[DelayCounterTimeOnHit]]**  |
| uint8 | **[[HasHit]]**  |
| float | **[[HasHitTime]]**  |
| uint8 | **[[HitWasBlocked]]**  |
| FName | **[[PreviousCombatState]]**  |
| uint8 | **[[PreviousHasHit]]**  |
| float | **[[PreviousHasHitTime]]**  |
| uint8 | **[[PreviousHitWasBlocked]]**  |
| float | **[[PreviousStateTime]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200