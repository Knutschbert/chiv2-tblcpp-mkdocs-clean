---
title: UCameraModifier_ArrowCam
type: class
aliases: UCameraModifier_ArrowCam
share: false

---

# UCameraModifier_ArrowCam





Inherits from UCameraModifier

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[ArrowCamPressed]]**() |
| void | **[[ArrowCamReleased]]**() |
| | **[[UCameraModifier_ArrowCam]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[OnFakeClientAttached]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * ParentItem) |
| void | **[[UpdateCharacterMesh]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[Projectile]]**  |
| bool | **[[bArrowCamPressed]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| UInputComponent * | **[[InputComponent]]**  |
| FRotator | **[[LastTargetRotation]]**  |
| FVector | **[[SmoothOffset]]**  |
| FRotator | **[[SmoothRotation]]**  |
| float | **[[TimeAfterCollision]]**  |
| FTransform | **[[TransformOnCollision]]**  |
| bool | **[[bFakeClientStopped]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200