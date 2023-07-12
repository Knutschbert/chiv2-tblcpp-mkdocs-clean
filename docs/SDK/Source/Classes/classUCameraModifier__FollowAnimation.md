---
title: UCameraModifier_FollowAnimation
type: class
aliases: UCameraModifier_FollowAnimation
share: false

---

# UCameraModifier_FollowAnimation





Inherits from UCameraModifier

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[Cancel]]**() |
| bool | **[[ShouldBlend]]**(FRotator ControlRot, FRotator SocketRot) |
| | **[[UCameraModifier_FollowAnimation]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[AnimationPitch]]**  |
| float | **[[AnimationYaw]]**  |
| [FFollowAnimationBlend](/docs/SDK/Source/Classes/structFFollowAnimationBlend.md) | **[[BlendInParams]]**  |
| [FFollowAnimationBlend](/docs/SDK/Source/Classes/structFFollowAnimationBlend.md) | **[[BlendOutParams]]**  |
| [FFollowAnimationBlend](/docs/SDK/Source/Classes/structFFollowAnimationBlend.md) | **[[CancelBlendOutParams]]**  |
| FRotator | **[[PrevBlendRot]]**  |
| float | **[[PrevSocketPitch]]**  |
| float | **[[PrevSocketYaw]]**  |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[TargetCharacter]]**  |
| bool | **[[bFollowPitch]]**  |
| bool | **[[bFollowYaw]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200