---
title: UVotingInstance
type: class
aliases: UVotingInstance
share: false

---

# UVotingInstance





Inherits from UActorComponent, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

Inherited by [UKickVotingInstance](/docs/SDK/Source/Classes/classUKickVotingInstance.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[[CanHaveMoreThanOneValid]]**() |
| bool | **[[CanPlayerBeParticipant]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * Voter) const |
| bool | **[[CanPlayerVote]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * Voter, FName VoteOption) const |
| bool | **[[CanVoteOccur]]**([ATBLPlayerController](/docs/SDK/Source/Classes/classATBLPlayerController.md) * InstigatingControlle, FName VoteOption) const |
| [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * | **[[GetInstigator]]**() const |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| int32 | **[[GetNumVotesForOption]]**(FName VoteOption) |
| int32 | **[[GetNumberOfVotes]]**() |
| FName | **[[GetPlayerVote]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * Voter) const |
| float | **[[GetStartTime]]**() const |
| float | **[[GetTimeLeft]]**() |
| int32 | **[[GetVotesNeededToPass]]**() |
| bool | **[[IsValidForVoter]]**([ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * Voter) |
| | **[[UVotingInstance]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| FName | **[[GetCurrentWinningOption]]**() |
| bool | **[[GetIsVoteFinished]]**() |
| TArray< [FVotingOption](/docs/SDK/Source/Classes/structFVotingOption.md) > | **[[GetVoteOptions]]**() |
| void | **[[OnRep_VoteOptions]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [FReplicated_ATBLPayerState](/docs/SDK/Source/Classes/structFReplicated__ATBLPayerState.md) | **[[InstigatorPlayer]]**  |
| FAfterVoteTimerSignature | **[[OnAfterVoteTimerFinished]]**  |
| FVoteConcludedSignature | **[[OnVoteConcluded]]**  |
| FVotesReplicated | **[[OnVotesReplicated]]**  |
| [FReplicated_Float](/docs/SDK/Source/Classes/structFReplicated__Float.md) | **[[StartTime]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[AfterVoteWaitTime]]**  |
| [FReplicated_FName](/docs/SDK/Source/Classes/structFReplicated__FName.md) | **[[CurrentWinningOption]]**  |
| float | **[[MinimumVoteTime]]**  |
| [FReplicatedArray_FVotingOption](/docs/SDK/Source/Classes/structFReplicatedArray__FVotingOption.md) | **[[VoteOptions]]**  |
| float | **[[VoteTime]]**  |
| [FReplicated_UInt8](/docs/SDK/Source/Classes/structFReplicated__UInt8.md) | **[[bIsVoteFinished]]**  |
| bool | **[[bVotesHaveMinimumTime]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:01 +0200