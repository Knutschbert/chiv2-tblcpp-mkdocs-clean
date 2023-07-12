---
title: UTextureAtlasManager
type: class
aliases: UTextureAtlasManager
share: false

---

# UTextureAtlasManager





Inherits from UObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[OnAssetCacheComplete]]**(URuntimeAssetCacheBuilder_ObjectBase * CachedAssetBuilder, bool Success) |
| | **[[UTextureAtlasManager]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< UTexture2D * > | **[[BuiltTextures]]**  |
| UMaterialInstanceDynamic * | **[[HeraldryRenderMID]]**  |
| UMaterialInstanceDynamic * | **[[OriginalHelmetMID]]**  |
| TArray< UObject * > | **[[ReferencedObjects]]**  |
| UTextureRenderTarget2D * | **[[RenderTargetForHeraldry]]**  |
| UTextureRenderTarget2D * | **[[RenderTargetForTextureType]]**  |
| UTextureRenderTarget2D * | **[[RenderTargetTemp]]**  |
| TArray< FName > | **[[RuntimeMorphTargets]]**  |
| bool | **[[bHeraldryRenderTargetInitialized]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:01 +0200