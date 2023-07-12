---
title: UEventCombatStateChanged
type: class
aliases: UEventCombatStateChanged
share: false

---

# UEventCombatStateChanged





Inherits from [UTriggeredAction](/docs/SDK/Source/Classes/classUTriggeredAction.md), [UAction](/docs/SDK/Source/Classes/classUAction.md), [UTBLObject](/docs/SDK/Source/Classes/classUTBLObject.md), [UAssemblyObject](/docs/SDK/Source/Classes/classUAssemblyObject.md), UObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[OnCombatStateChanged]]**(AActor * Actor, FName PreviousState, FName NewState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * InCombatState) |
| | **[[UEventCombatStateChanged]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| int32 | **[[AttackID]]**  |
| FName | **[[CombatState]]**  |
| FName | **[[CombatStateTag]]**  |
| uint8 | **[[bTriggerOnEnd]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200