---
title: AMultiActorHUDMarkerBase
type: class
aliases: AMultiActorHUDMarkerBase
share: false

---

# AMultiActorHUDMarkerBase





Inherits from AActor, [IHUDMarkerInterface](/docs/SDK/Source/Classes/classIHUDMarkerInterface.md), [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

Inherited by [AMultiActorHUDMarker](/docs/SDK/Source/Classes/classAMultiActorHUDMarker.md), [AMultiActorHUDMarkerAmmoRefill](/docs/SDK/Source/Classes/classAMultiActorHUDMarkerAmmoRefill.md), [AMultiActorHUDMarkerBurnable](/docs/SDK/Source/Classes/classAMultiActorHUDMarkerBurnable.md), [AMultiActorHUDMarkerInteractable](/docs/SDK/Source/Classes/classAMultiActorHUDMarkerInteractable.md), [AMultiActorHUDMarkerStatsComponent](/docs/SDK/Source/Classes/classAMultiActorHUDMarkerStatsComponent.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[AMultiActorHUDMarkerBase]]**() |
| void | **[[ActivateMarker]]**() |
| void | **[[AddMarkedActor]]**(AActor * Actor) |
| void | **[[AuthorityAddMarkedActor]]**(AActor * Actor) |
| void | **[[AuthorityRemoveMarkedActor]]**(AActor * Actor) |
| void | **[[AuthoritySetMarkedActors]]**(const TArray< AActor * > & InMarkedActors) |
| void | **[[DeactivateMarker]]**() |
| [UActorInfoDisplayComponent](/docs/SDK/Source/Classes/classUActorInfoDisplayComponent.md) * | **[[GetActorInfoComponent]]**() const |
| [UHudMarkerDisplayComponent](/docs/SDK/Source/Classes/classUHudMarkerDisplayComponent.md) * | **[[GetHUDMarkerComponent]]**() const |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| TArray< [UHudMarkerDisplayComponent](/docs/SDK/Source/Classes/classUHudMarkerDisplayComponent.md) * > | **[[GetMarkedActorHUDMarkerComponents]]**() |
| [UObjectiveStatusDisplayComponent](/docs/SDK/Source/Classes/classUObjectiveStatusDisplayComponent.md) * | **[[GetObjectiveStatusComponent]]**() const |
| TArray< [UWidgetVisibilityComponent](/docs/SDK/Source/Classes/classUWidgetVisibilityComponent.md) * > | **[[GetWidgetVisibilityComponents]]**() |
| bool | **[[IsActive]]**() const |
| bool | **[[IsVisible]]**() const |
| bool | **[[K2_ShouldIgnoreMarkedActor]]**(AActor * Actor) |
| void | **[[OnAuthorityAddedActorDestroyed]]**(AActor * Actor) |
| void | **[[RemoveMarkedActor]]**(AActor * Actor) |
| void | **[[SetMarkedActors]]**(const TArray< AActor * > & InMarkedActors) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[BindToObjectiveZone]]**() |
| void | **[[OnExtraMarkerDisplayExpired]]**() |
| void | **[[OnInitialVisibilityExpired]]**() |
| void | **[[OnPawnPossessed]]**(APawn * Pawn) |
| void | **[[OnPlayerEnteredZoneChanged]]**(bool bLocalPlayerInsideZone) |
| void | **[[OnRep_bIsEnabled]]**() |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [UActorInfoDisplayComponent](/docs/SDK/Source/Classes/classUActorInfoDisplayComponent.md) * | **[[ActorInfoComponent]]**  |
| int32 | **[[CurrentNumberOfMarkers]]**  |
| float | **[[DotProductScoreMultiplier]]**  |
| float | **[[ExtraMarkerDisplayDuration]]**  |
| FTimerHandle | **[[ExtraMarkerDisplayHandle]]**  |
| [FMultiActorHudMarkerArray](/docs/SDK/Source/Classes/structFMultiActorHudMarkerArray.md) | **[[FastReplicatedActors]]**  |
| [UHudMarkerDisplayComponent](/docs/SDK/Source/Classes/classUHudMarkerDisplayComponent.md) * | **[[HUDMarkerComponent]]**  |
| FTimerHandle | **[[InitialVisibilityHandle]]**  |
| TArray< TWeakObjectPtr< AActor > > | **[[LastDisplayedActorList]]**  |
| TMap< uint64, TWeakObjectPtr< AActor > > | **[[ManagedActorMap]]**  |
| TMap< uint64, TWeakObjectPtr< [UWidgetVisibilityComponent](/docs/SDK/Source/Classes/classUWidgetVisibilityComponent.md) > > | **[[ManagedComponentMap]]**  |
| int32 | **[[NumberOfMarkersToDisplay]]**  |
| int32 | **[[NumberOfMarkersToDisplayOnZoneVisible]]**  |
| [UObjectiveStatusDisplayComponent](/docs/SDK/Source/Classes/classUObjectiveStatusDisplayComponent.md) * | **[[ObjectiveStatusComponent]]**  |
| AActor * | **[[ObjectiveZoneActor]]**  |
| EObjectiveZoneVisibilityMode | **[[ObjectiveZoneVisibilityMode]]**  |
| TWeakObjectPtr< [UObjectiveZoneDisplayComponent](/docs/SDK/Source/Classes/classUObjectiveZoneDisplayComponent.md) > | **[[OwningObjectiveZoneComponent]]**  |
| bool | **[[bIsEnabled]]**  |
| bool | **[[bPlayerIsInOwningZone]]**  |
| bool | **[[bStartEnabled]]**  |
| bool | **[[bUseLegacyMode]]**  |
| bool | **[[bUseMarkedRadius]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200