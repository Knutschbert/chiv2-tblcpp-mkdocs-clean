---
title: UUtilityAI_TargetGenerator
type: class
aliases: UUtilityAI_TargetGenerator
share: false

---

# UUtilityAI_TargetGenerator





Inherits from UObject

Inherited by [UTG_ActorsWithAITag](/docs/SDK/Source/Classes/classUTG__ActorsWithAITag.md), [UTG_ActorsWithTag](/docs/SDK/Source/Classes/classUTG__ActorsWithTag.md), [UTG_BlackboardValue](/docs/SDK/Source/Classes/classUTG__BlackboardValue.md), [UTG_CharactersWithinRangeOfMe](/docs/SDK/Source/Classes/classUTG__CharactersWithinRangeOfMe.md), [UTG_DestinationVolume_WithAITag](/docs/SDK/Source/Classes/classUTG__DestinationVolume__WithAITag.md), [UTG_InsideCombatZone](/docs/SDK/Source/Classes/classUTG__InsideCombatZone.md), [UTG_OwnCharacter](/docs/SDK/Source/Classes/classUTG__OwnCharacter.md), [UTG_OwnLocation](/docs/SDK/Source/Classes/classUTG__OwnLocation.md), [UTG_OwnPawn](/docs/SDK/Source/Classes/classUTG__OwnPawn.md), [UTG_PerceivedCharacters](/docs/SDK/Source/Classes/classUTG__PerceivedCharacters.md), [UTG_PointsOnGrid](/docs/SDK/Source/Classes/classUTG__PointsOnGrid.md), [UTG_PointsWithinActorBounds](/docs/SDK/Source/Classes/classUTG__PointsWithinActorBounds.md), [UTG_RallyPoints](/docs/SDK/Source/Classes/classUTG__RallyPoints.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| TArray< AActor * > | **[[GetTargetActors]]**(const [FUtilityAI_Context](/docs/SDK/Source/Classes/structFUtilityAI__Context.md) & C) const |
| void | **[[GetTargetHybridLocations]]**(const [FUtilityAI_Context](/docs/SDK/Source/Classes/structFUtilityAI__Context.md) & C, TArray< [FUtilityAITargetHybrid](/docs/SDK/Source/Classes/structFUtilityAITargetHybrid.md) > & Locations) const |
| TArray< FVector > | **[[GetTargetLocations]]**(const [FUtilityAI_Context](/docs/SDK/Source/Classes/structFUtilityAI__Context.md) & C) const |
| TArray< UObject * > | **[[GetTargetObjects]]**(const [FUtilityAI_Context](/docs/SDK/Source/Classes/structFUtilityAI__Context.md) & C) const |
| bool | **[[IsValidTarget]]**(const [FUtilityAI_Context](/docs/SDK/Source/Classes/structFUtilityAI__Context.md) & Context) const |
| | **[[UUtilityAI_TargetGenerator]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| EUtilityAI_TargetType | **[[Type]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:01 +0200