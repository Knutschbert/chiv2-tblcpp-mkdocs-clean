---
title: UCustomizationComponent
type: class
aliases: UCustomizationComponent
share: false

---

# UCustomizationComponent





Inherits from [UTBLComponent](/docs/SDK/Source/Classes/classUTBLComponent.md), [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md), UActorComponent

## Public Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[[FindPreset]]**([FCustomizationPreset](/docs/SDK/Source/Classes/structFCustomizationPreset.md) & OutPreset) |
| TArray< FPrimaryAssetId > | **[[GetCurrentCustomization]]**() |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| TArray< FPrimaryAssetId > | **[[GetPendingCustomization]]**() |
| | **[[UCustomizationComponent]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| bool | **[[CustomizationApplied]]**  |
| [FCustomizationData](/docs/SDK/Source/Classes/structFCustomizationData.md) | **[[CustomizationData]]**  |
| [FReplicated_FCustomizationPreset](/docs/SDK/Source/Classes/structFReplicated__FCustomizationPreset.md) | **[[CustomizationPreset]]**  |
| FOnCachedMeshApplied | **[[OnCachedMeshApplied]]**  |
| FOnCustomizationApplied | **[[OnCustomizationApplied]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200