---
title: AAbilityInvocation
type: class
aliases: AAbilityInvocation
share: false

---

# AAbilityInvocation





Inherits from AActor, [IInstancedObjectContainer](/docs/SDK/Source/Classes/classIInstancedObjectContainer.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[AAbilityInvocation]]**() |
| void | **[[AddInvocationActor]]**(FName ActorName, AActor * Actor) |
| int32 | **[[FindInvocationActor]]**(AActor * Actor) |
| void | **[[FindInvocationActors]]**(FName ActorName, TArray< AActor * > & OutActors) |
| void | **[[OnActorDestroyed]]**(AActor * Actor) |
| void | **[[RemoveInvocationActor]]**(AActor * Actor) |
| void | **[[Terminate]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| FName | **[[AbilitiesTableRow]]**  |
| [UAbilityActivationMethod](/docs/SDK/Source/Classes/classUAbilityActivationMethod.md) * | **[[ActivationMethod]]**  |
| int32 | **[[AttackID]]**  |
| TArray< FTimerHandle > | **[[AutonomousTimers]]**  |
| double | **[[CompletionTime]]**  |
| int32 | **[[Flags]]**  |
| int32 | **[[ID]]**  |
| [UAbilitySpec](/docs/SDK/Source/Classes/classUAbilitySpec.md) * | **[[InitiatedAbilitySpec]]**  |
| [FAbilityInitiationParams](/docs/SDK/Source/Classes/structFAbilityInitiationParams.md) | **[[InitiationParams]]**  |
| AActor * | **[[Initiator]]**  |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[InventoryItem]]**  |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[InventoryItemClass]]**  |
| TArray< [FInvocationActor](/docs/SDK/Source/Classes/structFInvocationActor.md) > | **[[InvocationActors]]**  |
| [FInvocationComplete](/docs/SDK/Source/Classes/structFInvocationComplete.md) | **[[InvocationEvent]]**  |
| [UAbilityInvocationRegistryComponent](/docs/SDK/Source/Classes/classUAbilityInvocationRegistryComponent.md) * | **[[InvocationRegistry]]**  |
| FInvocationCompleteSignature | **[[OnComplete]]**  |
| int32 | **[[RandomSeed]]**  |
| [UAbilityTargetMethod](/docs/SDK/Source/Classes/classUAbilityTargetMethod.md) * | **[[TargetMethod]]**  |
| bool | **[[bActivationMethodFinished]]**  |
| bool | **[[bActive]]**  |
| bool | **[[bCleanedUp]]**  |
| bool | **[[bClientComplete]]**  |
| bool | **[[bClientInvocation]]**  |
| bool | **[[bPendingCleanup]]**  |
| bool | **[[bTargetMethodFinished]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200