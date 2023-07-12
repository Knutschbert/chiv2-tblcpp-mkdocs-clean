---
title: ADestinationGeneratorVolume
type: class
aliases: ADestinationGeneratorVolume
share: false

---

# ADestinationGeneratorVolume





Inherits from AVolume

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[ADestinationGeneratorVolume]]**() |
| void | **[[Activate]]**() |
| void | **[[Deactivate]]**() |
| void | **[[GeneratePoints]]**() |
| FVector | **[[GetDestinationByIndex]]**(int32 Index) const |
| TArray< FVector > | **[[GetDestinationList]]**() const |
| TArray< FVector > | **[[GetDestinationsInGridDistance]]**(const FVector & QueryLocation, int32 GridDistance) const |
| FVector | **[[GetRandomDestination]]**() const |
| void | **[[ProjectDestinationListToNavMesh]]**() |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| FGameplayTagContainer | **[[AITagsToAddWhenActivated]]**  |
| float | **[[DestinationDensity]]**  |
| TArray< FVector > | **[[DestinationList]]**  |
| TArray< FVector > | **[[DestinationListRelative]]**  |
| float | **[[DestinationVariance]]**  |
| EGenerationMode | **[[GenerationMode]]**  |
| float | **[[NavMeshProjectionDepenetrationDistance]]**  |
| bool | **[[bIsActive]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200