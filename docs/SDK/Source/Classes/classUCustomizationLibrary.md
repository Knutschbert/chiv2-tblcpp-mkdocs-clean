---
title: UCustomizationLibrary
type: class
aliases: UCustomizationLibrary
share: false

---

# UCustomizationLibrary





Inherits from UBlueprintFunctionLibrary

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[ApplyAssets]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Char, UPARAM(Ref) TArray< FPrimaryAssetId > & InAssetIds) |
| void | **[[ApplyCustomizationToItem]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * NewItem, [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * PlaterState, EFaction Faction, TEnumAsByte< EAudioClassType::Type > Class) |
| void | **[[ApplyCutomizationToCharacter]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * InCharacter) |
| void | **[[ApplyRandomAsset]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Char, FPrimaryAssetType PrimaryAssetType) |
| void | **[[CustomizeHead]]**(AActor * HeadActor, const [FReplicated_FCustomizationPreset](/docs/SDK/Source/Classes/structFReplicated__FCustomizationPreset.md) & CustomizationPreset) |
| void | **[[EquipAssetsForClassFaction]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * PlayerState, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Char, TEnumAsByte< EAudioClassType::Type > ClassType, EFaction Faction, const TArray< FPrimaryAssetId > & InAssetIds, const TArray< TSubclassOf< [UCTBase](/docs/SDK/Source/Classes/classUCTBase.md) >> CTClassesToIgnore) |
| bool | **[[ForceAllMipLevelsOnMaterials]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * InCharacter, const FName InMeshName, const FName ParameterName, const FName SlotName, float Seconds) |
| void | **[[GetAllCharMesh]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Char, TArray< UMeshComponent * > & OutComponents) |
| void | **[[GetAllWeaponMesh]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Char, TArray< UMeshComponent * > & OutComponents) |
| USkeletalMeshComponent * | **[[GetBeardMesh]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Char, bool WantFirstPerson) |
| [UCTBase](/docs/SDK/Source/Classes/classUCTBase.md) * | **[[GetCustomizationAsset]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Char, TSubclassOf< [UCTBase](/docs/SDK/Source/Classes/classUCTBase.md) > CustomizationType, TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > WeaponClass) |
| USkeletalMeshComponent * | **[[GetHairMesh]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Char, bool WantFirstPerson) |
| USkeletalMeshComponent * | **[[GetHeadMesh]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Char, bool WantFirstPerson) |
| USkeletalMeshComponent * | **[[GetHelmetMesh]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Char, bool WantFirstPerson) |
| UStaticMeshComponent * | **[[GetInventoryMesh]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Char, const FSoftObjectPath & WeaponAsset, AActor *& ItemOut) |
| USkeletalMeshComponent * | **[[GetInventorySKMesh]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Char, const FSoftObjectPath & WeaponAsset, AActor *& ItemOut) |
| FSlateBrush | **[[GetItemIconFromAssetId]]**(FPrimaryAssetId PrimaryAsset) |
| FText | **[[GetItemNameFromAssetId]]**(FPrimaryAssetId PrimaryAsset) |
| USkeletalMeshComponent * | **[[GetLegsMesh]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Char, bool WantFirstPerson) |
| UClass * | **[[GetPrimaryAssetClass]]**(FPrimaryAssetId PrimaryAsset) |
| void | **[[GetRandomAssets]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Char, TArray< FPrimaryAssetId > & OutAssetIds) |
| void | **[[GetTattooCustomizationEnabled]]**(bool & Enabled) |
| USkeletalMeshComponent * | **[[GetTorsoMesh]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Char, bool WantFirstPerson) |
| EWeaponTag | **[[GetWeaponTagFromPrimaryAssetId]]**(FPrimaryAssetId PrimaryAsset) |
| void | **[[InitializeContext]]**(const TArray< FPrimaryAssetId > & AssetIds, [FCustomizationContext](/docs/SDK/Source/Classes/structFCustomizationContext.md) & Context) |
| bool | **[[LoadCustomizationPreset]]**(APawn * Pawn, [FCustomizationPreset](/docs/SDK/Source/Classes/structFCustomizationPreset.md) & InPreset) |
| void | **[[PreviewAssets]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * PlayerState, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Char, UClass * CharacterPresetClass, const FPrimaryAssetId & InAssetIdsToPreview) |
| FName | **[[PrimaryAssetIDToPreviewCamera]]**(const FPrimaryAssetId & AssetId) |
| void | **[[SaveAssetsForClassFaction]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * PlayerState, TEnumAsByte< EAudioClassType::Type > ClassType, EFaction Faction) |
| void | **[[SetBeardHidden]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Char, bool Hide) |
| bool | **[[SetColorParameterValueOnMaterials]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * InCharacter, const FName InMeshName, const FName InParameterName, const FLinearColor & InParameterValue) |
| void | **[[SetEarHidden]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Char, bool Hide) |
| void | **[[SetHairBeardEarHiddenFromContext]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Char, bool bUseItemsVisibilityForContext) |
| void | **[[SetHairHidden]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Char, bool Hide) |
| void | **[[SetHelmetHidden]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Char, bool Hide) |
| bool | **[[SetMeshAndMaterial]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * InCharacter, const FName InMeshName, USkeletalMesh * SrcMesh, UMaterialInterface * Material, const FName SlotName) |
| bool | **[[SetMorphTarget]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * InCharacter, const FName InMeshName, const FName MorphTargetName, float InValue) |
| void | **[[SetScalarParameterOnMaterials]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Char, const FName ParameterName, const float ParameterValue) |
| bool | **[[SetScalarParameterValueOnMaterials]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * InCharacter, const FName InMeshName, const FName InParameterName, float InParameterValue) |
| bool | **[[SetStaticMeshAndMaterial]]**(UStaticMeshComponent * SKM, UStaticMesh * SrcMesh, UMaterialInterface * Material, const FName SlotName) |
| bool | **[[SetTextureParameterValueOnMaterials]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * InCharacter, const FName InMeshName, const FName ParameterName, UTexture * ParameterValue, const FName SlotName) |
| void | **[[SetVectorParameterOnMaterials]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Char, const FName ParameterName, const FVector ParameterValue) |
| | **[[UCustomizationLibrary]]**() |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200