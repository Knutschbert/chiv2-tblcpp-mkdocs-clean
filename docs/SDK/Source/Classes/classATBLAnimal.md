---
title: ATBLAnimal
type: class
aliases: ATBLAnimal
share: false

---

# ATBLAnimal





Inherits from [ATBLCharacterBase](/docs/SDK/Source/Classes/classATBLCharacterBase.md), [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md), ACharacter, [ISignificanceInterface](/docs/SDK/Source/Classes/classISignificanceInterface.md)

Inherited by [ACarryablePig](/docs/SDK/Source/Classes/classACarryablePig.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[ATBLAnimal]]**() |
| void | **[[CarryableAnimalEvent]]**(FName EventName, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * ParentCharacter) |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| void | **[[K2_TornOff]]**() |
| void | **[[OnRep_bPanicking]]**() |
| void | **[[Ragdoll]]**() |
| void | **[[StartPanicking]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[CheckCharMoveTick]]**(const bool bAsync) |
| void | **[[OnDamageTaken]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & DamageEvent) |
| void | **[[OnKilled]]**(const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & DamageEvent) |
| void | **[[SetCharMoveTickingAllowed]]**(const bool bTickAllowed) |
| void | **[[StopPanicking]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [UTBLAnimalAnimInstance](/docs/SDK/Source/Classes/classUTBLAnimalAnimInstance.md) * | **[[AnimInstance]]**  |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[AnimalHolder]]**  |
| TSubclassOf< [UAnimationSet](/docs/SDK/Source/Classes/classUAnimationSet.md) > | **[[AnimationSet]]**  |
| float | **[[MaxHealth]]**  |
| float | **[[MaxPanicWalkSpeed]]**  |
| float | **[[MaxWalkSpeed]]**  |
| UPawnNoiseEmitterComponent * | **[[NoiseEmitter]]**  |
| float | **[[PanicDuration]]**  |
| [FReplicationPredictionState](/docs/SDK/Source/Classes/structFReplicationPredictionState.md) | **[[PredictionState]]**  |
| [UStatsComponent](/docs/SDK/Source/Classes/classUStatsComponent.md) * | **[[Stats]]**  |
| bool | **[[bIsBeingHeld]]**  |
| bool | **[[bIsBeingThrown]]**  |
| bool | **[[bPanicking]]**  |
| bool | **[[bReplicatePanicking]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| bool | **[[bCharMoveTickingAllowed]]**  |
| bool | **[[bIsSignificant]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200