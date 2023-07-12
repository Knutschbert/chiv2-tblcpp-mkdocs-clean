---
title: UAbilityTargetMethod
type: class
aliases: UAbilityTargetMethod
share: false

---

# UAbilityTargetMethod





Inherits from [UTBLObject](/docs/SDK/Source/Classes/classUTBLObject.md), [UAssemblyObject](/docs/SDK/Source/Classes/classUAssemblyObject.md), UObject

Inherited by [UCompositeTargetMethod](/docs/SDK/Source/Classes/classUCompositeTargetMethod.md), [UMeleeTargetMethod](/docs/SDK/Source/Classes/classUMeleeTargetMethod.md), [UShapeTargetMethod](/docs/SDK/Source/Classes/classUShapeTargetMethod.md), [USingleTargetMethod](/docs/SDK/Source/Classes/classUSingleTargetMethod.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| [FResult](/docs/SDK/Source/Classes/structFResult.md) | **[[CanInitiate]]**() const |
| void | **[[Cancel]]**() |
| void | **[[Finish]]**() |
| [AAbilityInvocation](/docs/SDK/Source/Classes/classAAbilityInvocation.md) * | **[[GetInvocation]]**() const |
| void | **[[Start]]**() |
| void | **[[StartAutonomous]]**() |
| void | **[[StartCosmetic]]**() |
| | **[[UAbilityTargetMethod]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| FVector | **[[ClampTargetLocationToGround]]**(AActor * InInitiator, FVector TargetLocation, float MaxRange, bool & bHitGround, bool bTraceComplex, float MaxGroundTraceZAllowance) |
| FString | **[[GetContextString]]**() const |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [FActionContext](/docs/SDK/Source/Classes/structFActionContext.md) | **[[Context]]**  |
| int32 | **[[Flags]]**  |
| TWeakObjectPtr< AActor > | **[[Initiator]]**  |
| int32 | **[[MultiTargetMethodIndex]]**  |
| TArray< [UAction](/docs/SDK/Source/Classes/classUAction.md) * > | **[[TargetActions]]**  |
| TArray< [UAction](/docs/SDK/Source/Classes/classUAction.md) * > | **[[TargetBlockedActions]]**  |
| FName | **[[TargetMethodName]]**  |
| TArray< [UCondition](/docs/SDK/Source/Classes/classUCondition.md) * > | **[[TargetPrerequisites]]**  |
| bool | **[[bDoParryBoxTrace]]**  |
| uint8 | **[[bFinished]]**  |
| bool | **[[bStarted]]**  |
| bool | **[[bUnblockable]]**  |
| uint8 | **[[bUndoActionsOnCancel]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [UAbilitySpec](/docs/SDK/Source/Classes/classUAbilitySpec.md) * | **[[AbilitySpec]]**  |
| TArray< TWeakObjectPtr< AActor > > | **[[AcquiredTargets]]**  |
| TWeakObjectPtr< [AAbilityInvocation](/docs/SDK/Source/Classes/classAAbilityInvocation.md) > | **[[Invocation]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200