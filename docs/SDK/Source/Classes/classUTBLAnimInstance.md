---
title: UTBLAnimInstance
type: class
aliases: UTBLAnimInstance
share: false

---

# UTBLAnimInstance





Inherits from UAnimInstance

Inherited by [UTBLAnimalAnimInstance](/docs/SDK/Source/Classes/classUTBLAnimalAnimInstance.md), [UTBLBallistaAnimInstance](/docs/SDK/Source/Classes/classUTBLBallistaAnimInstance.md), [UTBLBatteringRamAnimInstance](/docs/SDK/Source/Classes/classUTBLBatteringRamAnimInstance.md), [UTBLBombardAnimInstance](/docs/SDK/Source/Classes/classUTBLBombardAnimInstance.md), [UTBLCatapultAnimInstance](/docs/SDK/Source/Classes/classUTBLCatapultAnimInstance.md), [UTBLCharacterAnimInstance](/docs/SDK/Source/Classes/classUTBLCharacterAnimInstance.md), [UTBLCharacterMountableAnimInstance](/docs/SDK/Source/Classes/classUTBLCharacterMountableAnimInstance.md), [UTBLHorseAnimInstance](/docs/SDK/Source/Classes/classUTBLHorseAnimInstance.md), [UTBLWeaponAnimInstance](/docs/SDK/Source/Classes/classUTBLWeaponAnimInstance.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AnimNotify_ActivateAbility]]**() |
| void | **[[AnimNotify_EndWeaponTracers]]**() |
| void | **[[EventFarFromCameraChanged]]**() |
| void | **[[EventOnLODLevelChanged]]**() |
| TArray< [FAnimDebugMontageInstance](/docs/SDK/Source/Classes/structFAnimDebugMontageInstance.md) > | **[[GetDebugMontageInstances]]**() |
| bool | **[[Montage_IsAnyMontagePlayingOnSlot]]**(const FName SlotNodeName) const |
| float | **[[Montage_PlaySection]]**(UAnimMontage * MontageToPlay, FName StartingSection, float InPlayRate, float StartSectionPercent, float InBlendTime, EMontagePlayReturnType ReturnValueType) |
| void | **[[Montage_StopAll]]**(float InBlendOutTime) |
| void | **[[SetIsFarFromCamera]]**(bool bIsFar) |
| void | **[[SetLODLevel]]**(int32 NewLodLevel) |
| | **[[UTBLAnimInstance]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[DumpAnimationInfoToFile]]**() |
| void | **[[GatherDebugNodeVisit]]**() |
| TArray< FString > | **[[GetDebugNodeVisit]]**() |
| TArray< FString > | **[[GetDebugNodeVisit_Blend]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [UCombatStateComponent](/docs/SDK/Source/Classes/classUCombatStateComponent.md) * | **[[CombatStateComponent]]**  |
| float | **[[FarFromCameraDistance]]**  |
| bool | **[[IsFarFromCamera]]**  |
| int32 | **[[LODLevel]]**  |
| float | **[[LastUpdateAnimationInterval]]**  |
| float | **[[LastUpdateAnimationTime]]**  |
| FRandomStream | **[[RandStream]]**  |
| USkeletalMeshComponent * | **[[SkeletalMesh]]**  |
| bool | **[[bWantsUpdateAnimation]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TMap< FName, FName > | **[[CrowdControlVariant1]]**  |
| TMap< FName, FName > | **[[CrowdControlVariant2]]**  |
| TMap< FName, FName > | **[[CrowdControlVariant3]]**  |
| TArray< int32 > | **[[DebugAnimNodes]]**  |
| FString | **[[DebugNodeVisitFilter]]**  |
| TArray< FName > | **[[DefaultDebugCategories]]**  |
| TArray< FName > | **[[HideLowLodBones]]**  |
| TMap< FName, [FAnimDebugMontage](/docs/SDK/Source/Classes/structFAnimDebugMontage.md) > | **[[MontageDebug]]**  |
| TMap< FName, [FAnimDebugStateMachine](/docs/SDK/Source/Classes/structFAnimDebugStateMachine.md) > | **[[StateMachineDebug]]**  |
| TArray< FName > | **[[StateMachineNames]]**  |
| bool | **[[bDumpAnimationInfoToFile]]**  |
| bool | **[[bGatherDebugNodeVisit]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200