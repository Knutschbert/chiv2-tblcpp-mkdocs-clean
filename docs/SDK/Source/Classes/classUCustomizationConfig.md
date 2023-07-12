---
title: UCustomizationConfig
type: class
aliases: UCustomizationConfig
share: false

---

# UCustomizationConfig





Inherits from UObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[ApplySwatchToMID]]**(FName SwatchCategoryName, int32 SelectedSwatch, UMaterialInstanceDynamic * Mid, UMeshComponent * MeshComponent) |
| void | **[[GetCategories]]**(TArray< FName > & Categories) |
| void | **[[GetCategorySwatchAttachments]]**(FName Category, [UCustomizationComponent](/docs/SDK/Source/Classes/classUCustomizationComponent.md) * CustomizationComponent, TArray< TSubclassOf< [ACustomizationAttachment](/docs/SDK/Source/Classes/classACustomizationAttachment.md) >> & SwatchAttachments) |
| void | **[[GetCategorySwatchNames]]**(FName Category, TArray< FString > & SwatchNames) |
| int32 | **[[GetNumSwatchesInCategory]]**(FName Category) |
| void | **[[GetParametersAndMorphTargetsToApply]]**(FName Category, int32 SelectedSwatch, TArray< FName > & ScalarNames, TArray< float > & ScalarValues, TArray< FName > & VectorNames, TArray< FLinearColor > & VectorValues, TArray< FName > & TextureNames, TArray< UTexture * > & TextureValues, TArray< TSoftObjectPtr< UTexture >> & TextureReferenceValues, TArray< FName > & MorphTargetNames, TArray< float > & MorphTargetValues) |
| | **[[UCustomizationConfig]]**() |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200