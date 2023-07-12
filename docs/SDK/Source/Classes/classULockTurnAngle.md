---
title: ULockTurnAngle
type: class
aliases: ULockTurnAngle
share: false

---

# ULockTurnAngle





Inherits from UObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[OnCombatStateChanged]]**(AActor * Actor, FName PreviousState, FName NewState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * CombatState) |
| void | **[[OnCombatStateEvent]]**(AActor * InActor, FName EventName, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo) |
| void | **[[OnDelayTimer]]**(float OverTime) |
| void | **[[OnEndTimer]]**(float OverTime) |
| void | **[[OnRootMotionChanged]]**(bool bRootMotion) |
| | **[[ULockTurnAngle]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| int32 | **[[DelayTimerHandle]]**  |
| int32 | **[[EndTimerHandle]]**  |
| int32 | **[[HorizLockId]]**  |
| [FTurnLockParams](/docs/SDK/Source/Classes/structFTurnLockParams.md) | **[[TurnLock]]**  |
| int32 | **[[VertLockId]]**  |
| bool | **[[bEnabled]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200