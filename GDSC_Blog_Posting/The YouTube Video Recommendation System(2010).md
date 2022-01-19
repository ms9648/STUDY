# The YouTube Video Recommendation System
## <b> ABSTRACT </b>
We discuss the video recommendation system in use at YouTube, the world’s most popular online video community.

<b>우리는 세계에서 가장 인기있는 온라인 비디오 커뮤니티인 유튜브에서 사용하는 비디오 추천 시스템에 대해 이야기하고자 한다.</b>

The system recommends personalized sets of videos to users based on their activity on the site. 

<b>추천 시스템은 사용자가 사이트 내에서 활동한 내역을 바탕으로 개인화된 비디오 세트를 추천한다.</b>

We discuss some of the unique challenges that the system faces and how we address them. 

<b>우리는 시스템이 직면한 독특한 과제들과 그 해결 방법들에 대해 알아보고자 한다.</b>

In addition, we provide details on the experimentation and evaluation framework used to test and tune new algorithms. 

<b>게다가 새로운 알고리즘을 테스트하고 조정하는데 사용되는 실험과 평가 프레임워크에 대해 알려 줄 것이다.</b>

We also present some of the findings from
these experiments.

<b>또한 이러한 실험으로 부터 발견한 사실 중 몇 가지를 알려 줄 것이다.</b>

## <b>1. INTRODUCTION</b>
Personalized recommendations are a key method for information retrieval and content discovery in today’s informationrich environment. 

<b>개인화된 추천은 오늘날 같이 정보가 풍부한 사회에서 정보 검색과 컨텐츠 탐색을 위한 중요한 방법이다.</b>

Combined with pure search (querying) and browsing (directed or non-directed), they allow users facing a huge amount of information to navigate that information in an efficient and satisfying way. 

<b>단순 검색(querying)과 브라우징(directed or non-directed)을 함께 사용하면 사용자가 엄청난 양의 정보 속에서 효율적이고 만족스러운 방식으로 정보를 탐색할 수 있다.</b>

As the largest and most-popular online video community with vast amounts of user-generated content, YouTube presents some unique opportunities and challenges for content discovery and recommendations.

<b>유튜브는 방대한 양의 사용자 제작 콘텐츠를 보유한 가장 규모가 크고 가장 인기 있는 온라인 비디오 커뮤니티로서 콘텐츠 검색 및 추천에 대한 몇 가지 고유한 기회와 과제를 제시한다.</b>

Founded in February 2005, YouTube has quickly grown to be the world’s most popular video site. 

<b>2005년 2월에 설립된 유튜브는 빠르게 세계에서 가장 인기 있는 동영상 사이트로 성장했다.</b>


Users come to YouTube to discover, watch and share originally-created videos. 

<b>사용자들이 유튜브에 와서 원래 만들어진 영상을 찾아보고 보고 공유한다.</b>

YouTube provides a forum for people to engage with
video content across the globe and acts as a distribution platform for content creators. 

<b>유튜브는 전 세계 사람들이 동영상 콘텐츠에 참여할 수 있는 장을 제공하고 콘텐츠 제작자들을 위한 유통 플랫폼 역할을 한다.</b>

Every day, over a billion video plays are done across millions of videos by millions of users,and every minute, users upload more than 24 hours of video to YouTube.

<b>매일, 수백만 명의 사용자들이 수백만 개의 비디오에 걸쳐 10억 개 이상의 비디오 재생을 하고 있으며, 매 분마다 사용자들은 24시간 이상의 비디오를 유튜브에 업로드한다.</b>

In this paper, we present our video recommendation system, which delivers personalized sets of videos to signed in users based on their previous activity on the YouTube site (while recommendations are also available in a limited form to signed out users, we focus on signed in users for the remainder of this paper).

<b>본 논문에서, 우리는 유튜브 사이트에서의 이전 활동을 기반으로 로그인한 사용자에게 개인화된 비디오 세트를 제공하는 비디오 추천 시스템을 제시한다(추천은 로그인한 사용자에게 제한된 형태로도 제공되지만, 이 논문의 나머지 부분에서는 로그인한 사용자에게 초점을 맞춘다).</b>

Recommendations are featured in two primary locations: The YouTube home page (http://www.youtube.com) and the “Browse” page at http:
//www.youtube.com/videos.

<b>추천 시스템은 다음 두 곳에 있다:  
유튜브 홈페이지(http://www.youtube.com)  
브라우저 페이지(http://www.youtube.com/videos)</b>

An example of how recommendations are presented on the homepage can be found in Figure 1.

<b>홈페이지에서 추천이 어떻게 제공되는지에 대한 예시를 그림 1에서 확인할 수 있다.</b>

### <b>1.1 Goals</b>
Users come to YouTube for a wide variety of reasons which span a spectrum from more to less specific: To watch a single video that they found elsewhere (direct navigation), to find specific videos around a topic (search and goal-oriented
browse), or to just be entertained by content that they find interesting. 

<b>사람들은 다양한 방식으로 유튜브에 방문한다:
1. 다른 곳에서 유입된 경우(html 링크로 접속)
2. 특정 비디오를 찾고자 하는 경우  
3. 흥미 위주로 돌아다니는 경우</b>

Personalized Video Recommendations are one way to address this last use case, which we dub unarticulated want.

<b>개인화된 비디오 추천 시스템은 이러한 마지막 사용 사례를 해결하는 한 가지 방법이다.</b>

As such, the goal of the system is to provide personalized recommendations that help users find high quality videos relevant to their interests. 

<b>이와 같이, 이 시스템의 목표는 사용자들이 자신의 관심사에 맞는 고품질 동영상을 찾을 수 있도록 돕는 개인화된 추천을 제공하는 것이다.</b>

In order to keep users entertained and engaged, it is imperative that these recommendations are updated regularly and reflect a user’s recent activity on the site. 

<b>사용자를 즐겁게 하고 참여시키기 위해서는 이러한 추천 시스템을 정기적으로 업데이트하고 사이트에서 사용자의 최근 활동을 반영해야 한다.</b>

They are also meant to highlight the broad spectrum of content that is available on the site. 

<b>또한 사이트에서 이용할 수 있는 콘텐츠의 넓은 스펙트럼을 강조하기 위한 것이다.</b>

In its present form, our recommendation system is a top-N recommender rather than a predictor. 

<b>현재 우리의 추천 시스템은 예측이라기 보다는 상위 N개 추천 알고리즘을 사용한다.</b>

We review how we evaluate the success of the recommendation system in section 3 of this paper. 

<b>우리는 본 논문의 섹션 3에서 추천 시스템의 성공을 평가하는 방법을 검토할 것이다.</b>

An additional primary goal for YouTube recommendations is to maintain user privacy and provide explicit control over personalized user data that our backend systems expose. 

<b>YouTube 추천 시스템에 대한 추가적인 주요 목표는 사용자 개인 정보를 유지하고 백엔드 시스템이 노출하는 개인화된 사용자 데이터를 명시적으로 제어하는 것이다.</b>

We review how we address this goal in section 2.5.

<b>섹션 2.5에서 우리가 이 목표를 어떻게 접근하는지를 보고할 것이다.</b>


### <b>1.2 Challenges</b>
There are many aspects of the YouTube site that make recommending interesting and personally relevant videos to users a unique challenge: Videos as they are uploaded by users often have no or very poor metadata. 

<b>유튜브 사이트에는 사용자들에게 흥미롭고 개인적으로 관련 있는 동영상을 추천하는 것이 독특한 도전과제가 될 수 있는 많은 측면이 있다:  
사용자가 업로드하는 동영상은 메타데이터가 없거나 매우 불량한 경우가 많다.</b>

The video corpus size is roughly on the same order of magnitude as the number of active users.

<b>비디오 코퍼스의 크기는 활동중인 사용자 수와 거의 같은 크기이다.</b>

Furthermore, videos on YouTube are mostly short form (under 10 minutes in length). 

<b>게다가, 유튜브의 영상들은 대부분 짧은 형식(길이 10분 미만)이다.</b>

User interactions are thus relatively short and noisy. 

<b>따라서 사용자 상호 작용은 상대적으로 짧고 잡음이 많다.</b>

Compare this to user interactions with movie rental or purchase sites such as Netflix or Amazon where renting a movie or purchasing an item are very clear declarations of intent. 

<b>영화를 대여하거나 물건을 구입하는 것이 매우 명확한 의향을 나타내는 넷플릭스나 아마존과 같은 영화 대여 또는 구매 사이트와의 사용자 상호작용과 비교해보라.</b>

In addition, many of the interesting videos on YouTube have a short life cycle going from upload to viral in the order of days requiring constant freshness of recommendation.

<b>그 외에도 유튜브의 많은 흥미로운 영상들은 지속적인 추천 새로고침이 요구되며 업로드한 후 며칠 만에 바이럴로 가는 짧은 수명 주기를 가지고 있다.</b>

## <b>2. SYSTEM DESIGN</b>
The overall design of the recommendation system is guided by the goals and challenges outlined above: We want recommendations to be reasonably recent and fresh, as well as diverse and relevant to the user’s recent actions.

<b>추천 시스템의 전반적인 설계는 위에 요약된 목표와 과제에 의해 안내된다:  
우리는 추천이 합리적으로 최신적이고 신선할 뿐만 아니라 다양하고 사용자의 최근 행동과 관련이 있기를 원한다.</b>

In addition, it’s important that users understand why a video was recommended to them.

<b>또한 사용자가 동영상을 추천받은 이유를 이해하는 것이 중요하다.</b>

The set of recommended videos videos is generated by using a user’s personal activity (watched, favorited, liked videos) as seeds and expanding the set of videos by traversing a co-visitation based graph of videos. 

<b>추천 동영상 세트는 사용자의 개인 활동(시청, 즐겨찾기, 좋아하는 동영상)을 시드로 사용하고, 동영상 공동 방문 기반 그래프를 통해 동영상 세트를 확장해 생성된다.</b>

The set of videos is then ranked using a variety of signals for relevance and diversity.

<b>그런 다음 비디오 세트는 관련성과 다양성을 위해 다양한 신호를 사용하여 순위를 매긴다.</b>

From an engineering perspective, we want individual components of the system to be decoupled from each other, allowing them to be understood and debugged in isolation.

<b>엔지니어링 관점에서, 우리는 시스템의 개별 구성 요소를 서로 분리하여 그것들을 이해하고 분리하여 디버깅할 수 있기를 원한다.</b>

Given that our system is part of the larger YouTube ecosystem, recommendations also needs to be resilient to failure and degrade gracefully in case of partial failures. 

<b>우리 시스템이 더 큰 유튜브 생태계의 일부라는 점에서 추천시스템은 오류에 탄력적이고 부분적인 오류 발생 시 품위 있게 저하될 필요가 있다.(막 망가지지 않아야한다는 의미인듯 합니다.)</b>

As a consequence, we strive to minimize complexity in the overall system.

<b>그 결과, 우리는 전체 시스템의 복잡성을 최소화하기 위해 노력한다.</b>

### 2.1 Input data
During the generation of personalized video recommendations we consider a number of data sources. 

<b>개인화된 비디오 추천을 생성하는 동안 우리는 여러 데이터 소스를 고려한다.</b>

In general, there are two broad classes of data to consider: 
1) content data, such as the raw video streams and video metadata such as title, description, etc
2) user activity data, which can further be divided into explicit and implicit categories.

<b>일반적으로 고려해야 할 데이터에는 크게 두 종류가 있다.
1) 원시 비디오 스트림 및 비디오 메타데이터(제목, 설명 등)와 같은 콘텐츠 데이터
2) 명시적 범주와 암묵적 범주로 더 나눌 수 있는 사용자 활동 데이터</b>

Explicit activities include rating a video, favoriting/liking a video, or subscribing to an uploader. 

<b>명시적 활동에는 동영상 등급 매기기, 동영상 선호/좋아요, 업로더 구독 등이 포함된다.</b>

Implicit activities are datum generated as a result of users watching and interacting with videos, e.g., user started to watch a video and user watched a large portion of the video (long watch).

<b>암시적 활동은 사용자가 비디오를 시청하고 상호작용한 결과로 생성된 자료이다.  
예를 들어, 사용자가 비디오를 보기 시작하고 사용자가 비디오의 많은 부분을 시청했다는 사실이다(오랜 시간동안 시청한 경우).</b>

In all cases, the data that we have at our disposal is quite noisy: Video metadata can be non-existent, incomplete, outdated, or simply incorrect; user data only captures a fraction
of a user’s activity on the site and only indirectly measures a user’s engagement and happiness, e.g., the fact that a user watched a video in its entirety is not enough to conclude
that she actually liked it. 

<b>모든 경우에, 우리가 마음대로 사용할 수 있는 데이터는 상당히 잡음이 많다:  
사용자 데이터는 사이트에서의 사용자 활동의 일부만 캡처하고 간접적으로 사용자의 참여도와 행복도만 측정한다. 예를 들어, 사용자가 동영상 전체를 시청했다는 사실만으로는 그 사람이 실제로 그것을 좋아했다고 결론지을 수 없다.</b>

The length of the video and user engagement level all influence the signal quality. 

<b>비디오의 길이와 사용자 참여 수준은 모두 신호 품질에 영향을 미친다.</b>

Moreover, implicit activity data is generated asynchronously and can be incomplete, e.g., the user closes the browser before we receive a long-watch notification.

<b>또한 암시적 활동 데이터는 비동시적으로 생성되며 불완전할 수 있다. 예를 들어, 사용자가 long-watch notification을 받기 전에 브라우저를 닫는 경우가 있다.</b>

## <b>2.2 Related Videos</b>
One of the building blocks of the recommendation system is the construction of a mapping from a video vi to a set of similar or related videos Ri. 

<b>추천 시스템의 구성 요소 중 하나는 동영상 vi에서 유사하거나 관련된 동영상 세트로의 매핑 구성이다.</b>

In this context, we define 'similar videos' as those that a user is likely to watch after having watched the given seed video v.

<b>이러한 맥락에서, 우리는 '유사한 비디오'를 사용자가 주어진 시드 비디오 v를 본 후 볼 가능성이 높은 비디오로 정의한다.</b>

In order to compute the mapping we make use of a well-known technique known as association rule mining or co-visitation counts.

<b>매핑을 계산하기 위해 우리는 연관 규칙 마이닝 또는 공동 방문 횟수라고 알려진 잘 알려진 기술을 사용한다.</b>

Consider sessions of user watch activities on the site. 

<b>사이트에서 사용자가 시청하는 시간을 고려해보라.</b>

For a given time period (usually 24 hours), we count for each pair of videos (vi, vj ) how often they were co-watched within sessions. 

<b>주어진 시간(보통 24시간) 동안, 우리는 각 비디오 쌍(vi, vj )에 대해 세션 내에서 그들이 얼마나 자주 공동 감시되었는지를 계산한다.</b>

Denoting this co-visitation count by cij , we define the relatedness score of video vj to base video vi as:

r(vi, vj ) = cij  
f(vi, vj ) --- (1)

<b>cij로 공동 방문 횟수를 나타내면서, 비디오 vi에 기반하여 비디오 vj에 대한 관련성 점수를 정의한다.

r(vi, vj ) = cij  
f(vi, vj )
</b>

where ci and cj are the total occurrence counts across all sessions for videos vi and vj , respectively. 

<b>여기서 ci와 cj는 각각 비디오 vi 및 vj 에 대한 모든 세션의 총 발생 횟수이다.</b>

f(vi, vj ) is a normalization function that takes the “global popularity” of both the seed video and the candidate video into account. 

<b>f(vi, vj)는 시드 비디오와 후보 비디오의 "글로벌 인기도"를 고려한 정규화 함수이다.</b>

One of the simplest normalization functions is to
simply divide by the product of the videos’ global popularity: 
f(vi, vj ) = ci · cj . 

<b>가장 간단한 정규화 함수 중 하나는 단순히 비디오의 공통된 인기의 곱으로 나누는 것이다.</b>

Other normalization functions are possible. 

<b>다른 정규화 함수들도 사용가능하다.</b>

When using the simple product of cardinalities for normalization, ci is the same for all candidate related videos and can be ignored in our setting, so we are normalizing only by the
candidate’s global popularity. 

<b>카디널리티의 간단한 제품을 정규화에 사용할 경우, ci는 모든 후보군 관련 동영상과 동일하고 우리가 설정에서 무시할 수 있기 때문에 후보군의 공통된 인기에 의해서만 정규화되고 있다.</b>

This essentially favors less popular videos over popular ones.

<b>이것은 본질적으로 인기 있는 영상보다 덜 인기 있는 영상을 선호한다.</b>

We then pick the set of related videos Ri for a given seed video vi as the top N candidate videos ranked by their scores r(vi, vj ). 

<b>그런 다음 주어진 시드 비디오 vi에 대한 관련 비디오 세트를 점수 r(vi, vj )로 순위를 매긴 상위 N개 후보 비디오로 선택한다.</b>

Note that in addition to only picking the top N
videos, we also impose a minimum score threshold.

<b>상위 N개 비디오만 선택하는 것 외에도 최소 점수 임계값을 지정한다.</b>

Hence, there are many videos for which we will not be able to compute a reliable set of related videos this way because their overall view count  (and thereby co-visitation counts with other videos) is too low.

<b>따라서, 전체 조회 수(따라서 다른 비디오와의 공동 방문 횟수)가 너무 낮기 때문에 이러한 방식으로 신뢰할 수 있는 관련 비디오 세트를 계산할 수 없는 많은 비디오가 있다.</b>

In practice there are additional problems that need to be solved—presentation bias, noisy watch data, etc.—and additional data sources beyond co-visitation counts that can be used: 
sequence and time stamp of video watches, video metadata, etc.

<b>solved-presentation bias, noisy한 시청 비디오 등 여러 문제들이 있다. 그리고 공동 방문 횟수를 넘어 추가적인 데이터 소스들도 사용될 수 있다: time stamp, 메타데이터 등.  
(논문에는 자세히 기술하지 않았지만, candidates pool을 만들기 위해 time stamp, 메타데이터 등을 사용했다고 합니다)</b>

The related videos can be seen as inducing a directed graph over the set of videos: For each pair of videos (vi, vj ), there is an edge eij from vi to vj iff vj ∈ Ri, with the weight
of this edge given by (1).

<b> 이건 해석 못하겠..습니다........</b>

### <b>2.3 Generating Recommendation Candidates</b>
To compute personalized recommendations we combine
the related videos association rules with a user’s personal activity on the site: This can include both videos that were watched (potentially beyond a certain threshold), as well as videos that were explicitly favorited, “liked”, rated, or added to playlists. We call the union of these videos the seed set.

<b>개인화된 추천 시스템을 계산하기 위해 관련 비디오 연결 규칙을 사이트의 사용자 개인 활동과 결합한다:  
여기에는 (잠재적으로) 시청된 비디오뿐만 아니라 명시적으로 선호하는 비디오, "좋아요", 등급 또는 재생 목록에 추가된 비디오가 포함될 수 있다. 우리는 이 비디오들의 결합을 seed set 이라고 부른다.</b>

In order to obtain candidate recommendations for a given seed set S, we expand it along the edges of the related videos graph: For each video vi in the seed set consider its related videos Ri. 

<b>주어진 seed set S에 대한 후보 추천을 얻기 위해 관련 비디오 그래프의 가장자리를 따라 이를 확장한다. seed set의 각 비디오 vi에 대해 관련 비디오를 고려한다.</b>

<!--
We denote the union of these related video sets
as C1: C1(S) = [
    vi∈S
    Ri (2)
-->

In many cases, computing C1 is sufficient for generating a set of candidate recommendations that is large and diverse enough to yield interesting recommendations. 

<b>많은 경우에, C1을 계산하는 것은 흥미로운 추천을 산출하기에 충분히 크고 다양하다.</b>

However, in practice the related videos for any videos tend to be quite narrow, often highlighting other videos that are very similar to the seed video.

<b>그러나 실제로 모든 비디오에 대한 관련 비디오는 상당히 좁은 경향이 있으며(커버리지가 낮다), 종종 시드 비디오와 매우 유사한 다른 비디오를 강조한다.</b>

This can lead to equally narrow recommendations, which do achieve the goal of recommending content close to the user’s interest, but fail to recommend videos which are truly new to the user.

<b>이는 똑같이 좁은 추천으로 이어질 수 있는데, 이는 사용자의 관심사에 가까운 콘텐츠를 추천한다는 목표를 달성하지만 사용자에게 진정으로 새로운 비디오를 추천하지는 못한다.</b>

In order to broaden the span of recommendations, we expand the candidate set by taking a limited transitive closure over the related videos graph. 

<b>추천 범위를 넓히기 위해 관련 비디오 그래프에 대해 제한적인 전이적 폐쇄를 수행하여 후보 세트를 확대한다.</b>

Let Cn be defined as the set of videos reachable within a distance of n from any video in the seed set:
<!--
Cn(S) = [
    vi∈Cn−1
    Ri (3)
-->

<b>Cn을 seed set의 비디오로부터 n만큼의 거리 내에 도달할 수 있는 비디오 집합으로 정의한다.</b>

where C0 = S is the base case for the recursive definition (note that this yields an identical definition for C1 as equation (2)). 

<b>여기서 C0 = S가 default값이다. (C1에 대한 정의는 식 (2)와 동일하다).</b>

The final candidate set Cfinal of recommendations
is then defined as: 

<!--
Cfinal = ([
    N
    i=0
    Ci) \ S (4)
-->

<b>마지막 후보 세트인 Cfinal은 다음과 같이 정의된다.</b>

Due to the high branching factor of the related videos graph we found that expanding over a small distance yielded a broad and diverse set of recommendations even for users with a small seed set. 

<b>관련 비디오 그래프의 분기 요인이 높기 때문에 작은 거리로 확장하면 작은 시드 세트를 가진 사용자에게도 광범위하고 다양한 권장 사항이 생성된다는 것을 발견했다.</b>

Note that each video in the candidate set is associated with one or more videos in the seed
set. 

<b>후보 세트의 각 비디오는 시드 세트의 하나 이상의 비디오와 연결되어 있다.</b>

We keep track of these seed to candidate associations for ranking purposes and to provide explanations of the recommendations to the user.

<b>우리는 순위를 매기고 사용자에게 추천에 대한 설명을 제공하기 위해 후보 연관에 대한 이러한 시드를 유지한다.</b>

### <b>2.4 Ranking</b>
After the generation step has produced a set of candidate videos they are scored and ranked using a variety of signals.

<b>생성 단계가 완료되면 다양한 신호를 사용하여 점수를 매기고 순위를 매긴다.</b>

The signals can be broadly categorized into three groups corresponding to three different stages of ranking: 
1) video quality 
2) user specificity 
3) diversification

<b>신호는 크게 세 개의 그룹으로 분류할 수 있다:
1) video quality 
2) user specificity 
3) diversification
</b>

Video quality signals are those signals that we use to judge the likelihood that the video will be appreciated irrespective of the user. 

<b>Video quality 신호는 사용자에 관계없이 비디오가 인식될 가능성을 판단하기 위해 사용하는 신호이다.</b>

These signals include view count (the total number of times a video has been watched), the ratings of the video, commenting, favoriting and sharing activity around the video, and upload time.

<b>이러한 신호에는 조회 수(동영상이 시청된 총 횟수), 비디오의 등급, 댓글 달기, 비디오 주위의 활동 선호 및 공유, 업로드 시간이 포함된다.</b>

User specificity signals are used to boost videos that are closely matched with a user’s unique taste and preferences.

<b>User specificity 신호는 사용자 고유의 취향과 선호도와 밀접하게 일치하는 동영상을 활성화하는 데 사용된다.</b>

To this end, we consider properties of the seed video in the user’s watch history, such as view count and time of watch.

<b>이를 위해 사용자의 시청 기록에서 시청 수 및 시청 시간과 같은 시드 비디오의 속성을 고려한다.</b>

Using a linear combination of these signals we generate a ranked list of the candidate videos.

<b>이러한 신호의 선형 조합을 사용하여 후보 비디오의 순위 목록을 생성한다.</b>

Because we display only a small number of recommendations (between 4 and 60), we have to choose a subset of the list. 

<b>우리는 적은 수의 추천(4개 ~ 60개)만 표시하므로 목록의 하위 집합을 선택해야 한다.</b>

Instead of choosing just the most relevant videos we optimize for a balance between relevancy and diversity across categories.

<b>가장 관련성이 높은 비디오만 선택하는 대신 여러 범주에 걸친 관련성과 다양성 간의 균형을 위해 최적화됩니다.</b>

Since a user generally has interest in multiple different topics at differing times, videos that are too similar to each other are removed at this stage to further increase diversity. 

<b>사용자는 일반적으로 서로 다른 시간에 여러 주제에 관심을 가지기 때문에, 이 단계에서 서로 너무 유사한 동영상은 더 많은 다양성을 증가시키기 위해 제거한다.</b>

One simple way to achieve this goal is to impose constraints on the number of recommendations that are associated with a single seed video, or by limiting the number of recommendations from the same channel (uploader). 

<b>이 목표를 달성하는 한 가지 간단한 방법은 단일 시드 비디오와 관련된 추천 수에 제약을 가하거나 동일한 채널(업로더)의 추천 수를 제한하는 것이다.</b>

More sophisticated techniques based on topic clustering and content analysis can also be used.

<b>주제 클러스터링과 콘텐츠 분석에 기반한 보다 정교한 기법도 사용할 수 있다.</b>

### <b>2.5 User Interface</b>
Presentation of recommendations is an important part of the overall user experience.

<b>추천 영상의 노출은 전체적인 사용자 경험의 중요한 부분이다.</b>

Figure 1 shows how recommendations are currently presented on YouTube’s home page.

<b>그림 1은 현재 유튜브 홈페이지에서 추천이 어떻게 제시되고 있는지를 보여준다.</b>

There are a few features worth noting: First, all recommended videos are displayed with a thumbnail and their (possibly truncated) title, as well as information about video age and popularity. 

<b>주목할 만한 몇 가지 기능이 있다. 먼저 모든 권장 동영상이 썸네일 및 제목(잘릴 수 있음)과 함께 비디오 연령 및 인기에 대한 정보와 함께 표시된다.</b>

This is similar to other sections on the homepage and helps users decide quickly whether they are
interested in a video. 

<b>이는 홈페이지의 다른 섹션에도 유사하며 사용자가 동영상에 대한 관심 여부를 빠르게 결정할 수 있도록 도와준다.</b>

Furthermore, we add an explanation with a link to the seed video which triggered the recommendation. 

<b>또한 추천된 시드 비디오에 링크와 함께 설명을 추가한다.</b>

Last, we give users control over where and how
many recommendations they want to see on the homepage.

<b>마지막으로 홈페이지에서 사용자가 원하는 추천의 위치와 개수를 제어할 수 있다.</b>

As mentioned in section 2.4, we compute a ranked list of recommendations but only display a subset at serving time.

<b>섹션 2.4에서 언급한 것처럼, 우리는 추천의 순위 목록을 계산하지만 서비스 시간에는 하위 집합만 표시한다.</b>

This enables us to provide new and previously unseen recommendations every time the user comes back to the site, even if the underlying recommendations have not been recomputed.

<b>따라서 기본 추천이 다시 계산되지 않았더라도 사용자가 사이트에 돌아올 때마다 이전에 보지 못했던 새로운 추천을 제공할 수 있다.</b>

### <b>2.6 System Implementation</b>
We choose a batch-oriented pre-computation approach rather than on-demand calculation of recommendations. 

<b>우리는 추천 계산 결과를 on-demand방식 보다는 배치 방식으로 구현한다.</b>

This has the advantages of allowing the recommendation generation stage access to large amounts of data with ample amounts of CPU resources while at the same time allowing the serving of the pre-generated recommendations to be extremely low latency. 

<b>이는 추천 영상 발생 단계에서 충분한 양의 CPU 자원을 가진 대량의 데이터에 접근할 수 있는 동시에 사전 생성된 추천의 서비스 지연 시간이 매우 짧다는 장점이 있다.</b>

The most significant downside of this approach is
the delay between generating and serving a particular recommendation data set. 

<b>이 접근법의 가장 큰 단점은 특정 추천 데이터 세트의 생성과 제공 사이의 지연이다.</b>

We mitigate this by pipelining the recommendation generation, updating the data sets several times per day.

<b>우리는 추천 생성을 파이프라인으로 연결하고 하루에 여러 번 데이터 세트를 업데이트하여 이를 완화한다.</b>

The actual implementation of YouTube’s recommendation system can be divided into three main parts: 
1) data collection
2) recommendation generation
3) recommendation serving

<b>유튜브 추천 시스템의 실제 구현은 크게 3가지로 나눌 수 있다:
1) data collection
2) recommendation generation
3) recommendation serving</b>

The raw data signals previously mentioned in section 2.1 are initially deposited into YouTube’s logs. 

<b>앞서 섹션 2.1에서 언급한 raw 데이터 신호는 처음에 유튜브 로그에 저장된다.</b>

These logs are processed, signals extracted, and then stored on a per user basis in a Bigtable. 

<b>이러한 로그는 빅테이블에 사용자별로 처리, 신호 추출, 저장된다.</b>

We currently handle millions of users and tens of billions of activity events with a total footprint
of several terabytes of data.

<b>우리는 현재 수 테라바이트의 총 데이터 공간으로 수백만 명의 사용자와 수백억 개의 활동 이벤트를 처리하고 있다.</b>

Recommendations are generated through a series of MapReduces computations that walk through the user/video graph to accumulate and score recommendations as described in section 2.

<b>추천은 섹션 2에 설명된 추천을 누적하고 점수를 매기기 위해 사용자/비디오 그래프를 통해 일련의 MapReduces 계산으로 생성된다.</b>

The generated data set sizes are relatively small (on the order of Gigabytes) and can be easily served by simplified read-only Bigtable servers to YouTube’s webservers; the time to complete a recommendation request is mostly dominated by network transit time.

<b>생성된 데이터 세트 크기는 비교적 작으며(기가바이트 단위), 단순화된 read-only Bigtable 서버에서 유튜브의 웹 서버에 쉽게 제공할 수 있다.
추천 요청을 완료하는 데 걸리는 시간은 대부분 네트워크 전송 시간에 의해 좌우된다.</b>

## <b>3. EVALUATION</b>
In our production system we use live evaluation via A/B testing [5] as the main method for evaluating the performance of the recommendation system. 

<b>우리의 생산 시스템에서는 추천 시스템의 성능을 평가하기 위한 주요 방법으로 A/B 테스트를 통한 실시간 평가를 사용한다.</b>

In this method, live traffic is diverted into distinct groups where one group acts as the control or baseline and the other group is exposed to a new feature, data, or UI. 

<b>이 방법에서 라이브 트래픽은 한 그룹이 제어 또는 기준선 역할을 하고 다른 그룹은 새로운 기능, 데이터 또는 UI에 노출되는 별개의 그룹으로 전환된다.</b>

The two groups are then compared against one another over a set of predefined metrics and possibly swapped for another period of time to eliminate other factors. 

<b>그런 다음 두 그룹을 미리 정의된 메트릭 집합에 대해 서로 비교하고 다른 요소를 제거하기 위해 다른 기간 동안 스왑할 수 있다.</b>

The advantage of this approach is that evaluation takes place in the context of the actual website
UI. 

<b>이 접근 방식의 장점은 평가는 실제 웹 사이트 UI의 맥락에서 수행된다는 것입니다.</b>

It’s also possible to run multiple experiments in parallel and get quick feedback on all of them. 

<b>또한, 여러 실험을 병렬로 실행해 빠른 피드백을 받을 수도 있다.</b>

The downsides are that not all experiments have reasonable controls that can be used for comparison, the groups of users must have sufficient traffic to achieve statistically significant results in a timely manner and evaluation of subjective goals is limited
to the interpretation of a relatively small set of pre-defined metrics.

<b>단점은 모든 실험이 비교를 위해 사용될 수 있는 합리적인 통제력을 갖는 것은 아니며, 사용자 그룹은 적시에 통계적으로 유의한 결과를 달성하기에 충분한 트래픽을 가져야 하며, 주관적 목표의 평가는 상대적으로 작은 사전 정의된 메트릭 세트의 해석으로 제한된다는 것이다.</b>

To evaluate recommendation quality we use a combination of different metrics. 

<b>추천 품질을 평가하기 위해 서로 다른 메트릭의 조합을 사용한다.</b>

The primary metrics we consider include click through rate (CTR), long CTR (only counting
clicks that led to watches of a substantial fraction of the video), session length, time until first long watch, and recommendation coverage (the fraction of logged in users with
recommendations). 

<b>우리가 고려하는 주요 지표에는 클릭률(CTR), 긴 CTR(동영상의 상당 부분을 감시하게 된 클릭 횟수만 계산), 세션 길이, 첫 번째 long-watch까지의 시간 및 추천 범위(추천을 통해 로그인한 사용자의 비율)가 포함된다.</b>

We use these metrics to both track performance of the system at an ongoing basis as well as for
evaluating system changes on live traffic.

<b>우리는 이러한 측정 기준을 사용하여 지속적으로 시스템의 성능을 추적하고 실시간 트래픽의 시스템 변경을 평가한다.</b>

## <b>4. RESULTS</b>
The recommendations feature has been part of the YouTube homepage for more than a year and has been very successful in context of our stated goals.

<b>추천 기능은 1년 이상 유튜브 홈페이지의 일부였으며, 우리가 밝힌 목표와 관련하여 매우 성공적이었다.</b>

For example, recommendations account for about 60% of all video clicks from the home page.

<b>예를 들어, 추천은 홈 페이지의 모든 비디오 클릭의 약 60%를 차지한다.</b>

Comparing the performance of recommendations with othermodules on the homepage suffers from 
presentation bias (recommendations are placed at the top by default).

<b>홈페이지에서 추천 성과를 다른 모듈과 비교하면 노출 편향(추천 영상이 기본적으로 맨 위에 배치됨)이 심해진다.</b>

To adjust for this, we look at CTR metrics from the “browse” pages and compare recommendations to other algorithmically generated video sets: 
a) Most Viewed - Videos that have received the most number of views in a day
b) Top Favorited - Videos that the viewers have added to their collection of favorites 
c) Top Rated - Videos receiving most like ratings in a day.

<b>이를 조정하기 위해 "찾아보기" 페이지에서 CTR 메트릭을 살펴보고 알고리즘적으로 생성된 다른 비디오 세트와 추천 시스템을 비교한다.
1) 가장 많이 본 동영상 - 하루 중 가장 많은 조회 수를 받은 동영상
2) 가장 좋아하는 동영상 - 시청자가 즐겨찾기 목록에 추가한 동영상
3) 최고 등급 - 하루에 가장 많은 좋아요를 받는 비디오
</b>

We measured CTR for these sections over a period of 21 days. 

<b>우리는 21일 동안 이러한 섹션에 대한 CTR을 측정했다.</b>

Overall we find that co-visitation based recommendation performs at 207% of the baseline Most Viewed page when averaged over the entire period, while Top Favorited and Top Rated perform at similar levels or below the Most Viewed baseline. 

<b>전체적으로 공동 방문 기반 추천 시스템은 전체 기간 동안 평균으로 가장 많이 본 페이지의 207% 정도로 수행되며, 가장 많이 본 페이지와 가장 많이 본 기준선보다 낮은 수준에서 수행된다.</b>

See figure 2 for an illustration of how the relative CTR varies over the period of 3 weeks.

<b>3주간의 상대적인 CTR이 어떻게 변하는지 그림 2를 참고하라.</b>