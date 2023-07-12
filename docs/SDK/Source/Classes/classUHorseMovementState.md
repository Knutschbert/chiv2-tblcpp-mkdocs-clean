---
title: UHorseMovementState
type: class
aliases: UHorseMovementState
share: false

---

# UHorseMovementState





Inherits from [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md), [UAssemblyInstance](/docs/SDK/Source/Classes/classUAssemblyInstance.md), UObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[GearDown]]**() |
| void | **[[GearUp]]**() |
| bool | **[[GetBoostMode]]**() |
| bool | **[[GetControlMode]]**() |
| float | **[[GetCrusingSpeed]]**() |
| float | **[[GetCurrentForwardSpeed]]**() |
| [UHorseMovement](/docs/SDK/Source/Classes/classUHorseMovement.md) * | **[[GetHorseMovement]]**() |
| void | **[[GetInputDirection]]**(EHorseMovementInput & Direction, float & HeldTime) |
| void | **[[GetInputForward]]**(float & InputForwardOut, float & HeldTime) |
| void | **[[GetInputStrafe]]**(float & InputStrafe, float & HeldTime) |
| void | **[[GetInputTurn]]**(float & InputTurn, float & HeldTime) |
| bool | **[[GetInvertedBackwardStrafe]]**() |
| float | **[[GetMaxSpeed]]**(FName State) |
| float | **[[GetMinSpeed]]**(FName State) |
| float | **[[GetOrbitTurnScale]]**(float LookAtDistance, float StrafeSpeed, float TurnRate) |
| float | **[[GetSettleSpeed]]**(FName State) |
| float | **[[GetSpeed]]**(FName State, float Percent) |
| void | **[[GetTargetOrientationOffset]]**(float & Min, float & Max, EMovementDirection Direction) |
| float | **[[GetTurnInputScale]]**(EHorseTurnInput TurnInput, float OrientationOffset) |
| void | **[[ModifyAccelerationScale]]**(float Target, float InterpSpeed) |
| void | **[[ModifyTargetSpeed]]**(float Target) |
| void | **[[ModifyTurnRateScale]]**(float Target, float InterpSpeed) |
| void | **[[StrafeGearDown]]**() |
| void | **[[StrafeGearUp]]**() |
| void | **[[TurnTowardsCamera]]**(float TurnRate, float TurnRateWithInput) |
| | **[[UHorseMovementState]]**() |
| void | **[[UpdateMovement]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [UHorseMovement](/docs/SDK/Source/Classes/classUHorseMovement.md) * | **[[movement]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200