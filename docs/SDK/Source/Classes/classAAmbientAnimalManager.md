---
title: AAmbientAnimalManager
type: class
aliases: AAmbientAnimalManager
share: false

---

# AAmbientAnimalManager





Inherits from [ATBLActor](/docs/SDK/Source/Classes/classATBLActor.md), AActor, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[AAmbientAnimalManager]]**() |
| void | **[[FleeAnimals]]**(FVector InstigatorLocation) |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| void | **[[HideAnimals]]**() |
| void | **[[RegenerateAndReseedAnimalActors]]**() |
| void | **[[ReseedAnimalActors]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[OnRep_FleeData]]**() |
| void | **[[PopAnimal]]**(EAnimalPopType Type) |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< [FAnimalConfig](/docs/SDK/Source/Classes/structFAnimalConfig.md) > | **[[AmbientAnimalList]]**  |
| TArray< AActor * > | **[[CachedAmbientAnimalList]]**  |
| [FFleeData](/docs/SDK/Source/Classes/structFFleeData.md) | **[[FleeData]]**  |
| float | **[[GeneratingRadius]]**  |
| UAIPerceptionComponent * | **[[PerceptionComponent]]**  |
| TArray< AActor * > | **[[RemainingAmbientAnimalList]]**  |
| USphereComponent * | **[[SphereComponent]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200