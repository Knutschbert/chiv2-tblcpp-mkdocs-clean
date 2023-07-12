---
title: UAction
type: class
aliases: UAction
share: false

---

# UAction





Inherits from [UTBLObject](/docs/SDK/Source/Classes/classUTBLObject.md), [UAssemblyObject](/docs/SDK/Source/Classes/classUAssemblyObject.md), UObject

Inherited by [UAbilityCost](/docs/SDK/Source/Classes/classUAbilityCost.md), [UAddMovementModifier](/docs/SDK/Source/Classes/classUAddMovementModifier.md), [UApplyCondition](/docs/SDK/Source/Classes/classUApplyCondition.md), [UApplyTargetMethod](/docs/SDK/Source/Classes/classUApplyTargetMethod.md), [UBlockedDamage](/docs/SDK/Source/Classes/classUBlockedDamage.md), [UConditionalActions](/docs/SDK/Source/Classes/classUConditionalActions.md), [UCrowdControl](/docs/SDK/Source/Classes/classUCrowdControl.md), [UDelay](/docs/SDK/Source/Classes/classUDelay.md), [UDropItem](/docs/SDK/Source/Classes/classUDropItem.md), [UEnableInteractableComponent](/docs/SDK/Source/Classes/classUEnableInteractableComponent.md), [ULoadItem](/docs/SDK/Source/Classes/classULoadItem.md), [UStandardDamage](/docs/SDK/Source/Classes/classUStandardDamage.md), [UStartJump](/docs/SDK/Source/Classes/classUStartJump.md), [UStartMovement](/docs/SDK/Source/Classes/classUStartMovement.md), [UTriggeredAction](/docs/SDK/Source/Classes/classUTriggeredAction.md), [UUseItem](/docs/SDK/Source/Classes/classUUseItem.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[UAction]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [FActionContext](/docs/SDK/Source/Classes/structFActionContext.md) | **[[Context]]**  |
| int32 | **[[Flags]]**  |
| TWeakObjectPtr< UObject > | **[[Initiator]]**  |
| TWeakObjectPtr< UObject > | **[[Target]]**  |
| FVector | **[[TargetLocation]]**  |
| int32 | **[[Version]]**  |
| bool | **[[bLogEvents]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| bool | **[[bIsComplete]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200