---
title: UMovementInstance
type: class
aliases: UMovementInstance
share: false

---

# UMovementInstance





Inherits from [UAssemblyInstance](/docs/SDK/Source/Classes/classUAssemblyInstance.md), UObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| [ATBLCharacterBase](/docs/SDK/Source/Classes/classATBLCharacterBase.md) * | **[[GetCharacterOwner]]**() const |
| void | **[[StartMovement]]**([UMovementSequence](/docs/SDK/Source/Classes/classUMovementSequence.md) * MovementSeq) |
| void | **[[Stop]]**() |
| | **[[UMovementInstance]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[OnActorHit]]**(AActor * SelfActor, AActor * OtherActor, FVector NormalImpulse, const FHitResult & Hit) |
| void | **[[OnCharacterHit]]**(AActor * Owner, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * HitCharacter) |
| void | **[[OnWallHit]]**(AActor * Owner, AActor * HitActor, float HitAngle) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [FMovementActionInitiationParams](/docs/SDK/Source/Classes/structFMovementActionInitiationParams.md) | **[[InitParams]]**  |
| float | **[[InitTime]]**  |
| FMovementInstanceDelegate | **[[OnFinishMovement]]**  |
| FMovementInstanceDelegate | **[[OnStartMovement]]**  |
| float | **[[ScalingFactor]]**  |
| [UMovementSequence](/docs/SDK/Source/Classes/classUMovementSequence.md) * | **[[Sequence]]**  |
| AActor * | **[[TargetActor]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [UMovementAction](/docs/SDK/Source/Classes/classUMovementAction.md) * | **[[CurrentMovement]]**  |
| float | **[[FinishTime]]**  |
| TArray< [UTBLObject](/docs/SDK/Source/Classes/classUTBLObject.md) * > | **[[InstancedObjects]]**  |
| bool | **[[bIsFinished]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200