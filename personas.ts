/*
    Persona types:
        - METABUDDY
        - METABUDDY_RYAN
        - TRAVEL_LUCAS
        - TRAVEL_SOPHIE
        - HOTEL_AMANDA
        - AIRPORT_LAURA
        - RESTAURANT_MIKE
        - HOSPITAL_SUSAN
        - INTERVIEW
        - WORK_JAMES
        - WORK_ANNA
*/

type AIPersonaType = {
    personaTypeName: string // "METABUDDY" | "METABUDDY_RYAN" | "INTERVIEW" | "CUSTOM" and more!
    nameEndKorean: string // "과" | "와"

    title: string
    description: string

    colors: string[]

    defaultAIName: string
    defaultAvatarUrl: string

    voiceId: string
}


const metabuddy_jane: AIPersonaType = {
    personaTypeName: "METABUDDY_JANE",
    nameEndKorean: "과",
    title: "다정한 Jane",
    description: "당신의 얘길 잘 들어주는 다정한 친구예요. 차분하고 싶은 날엔 Jane과 얘기해봐요.",
    colors: ["#ffdbef", "#ffdbef"],
    defaultAIName: "Jane",
    defaultAvatarUrl: "",
    voiceId: "",
}


const metabuddy_ryan: AIPersonaType = {
    personaTypeName: "METABUDDY_RYAN",
    nameEndKorean: "과",
    title: "유머러스한 Ryan",
    description: "Ryan은 긍정적인 바이브가 가득해요. 에너지를 받고 싶을 땐 Ryan 소환!",
    colors: ["#ffdbef", "#ffdbef"],
    defaultAIName: "Ryan",
    defaultAvatarUrl: "",
    voiceId: "",
}


const tourism_lucas: AIPersonaType = {
    personaTypeName: "TOURISM_LUCAS",
    nameEndKorean: "와",
    title: "친화력 좋은 Lucas",
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",
    colors: ["#ffdbef", "#ffdbef"],
    defaultAIName: "Lucas",
    defaultAvatarUrl: "https://models.readyplayer.me/63d1e63b23fe23d34bf6f226.glb",
    voiceId: "",
}


const tourism_sophie: AIPersonaType = {
    personaTypeName: "TOURISM_SOPHIE",
    nameEndKorean: "과",
    title: "활발한 Sophie",
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",
    colors: ["#ffdbef", "#ffdbef"],
    defaultAIName: "sophie",
    defaultAvatarUrl: "https://models.readyplayer.me/64115d0037dc29db74636509.glb",
    voiceId: "",
}


const hotel_amanda: AIPersonaType = {
    personaTypeName: "HOTEL_AMANDA",
    nameEndKorean: "와",
    title: "친절한 Amanda",
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",
    colors: ["#ffdbef", "#ffdbef"],
    defaultAIName: "Amanda",
    defaultAvatarUrl: "https://models.readyplayer.me/63d1e84223fe23d34bf6f3ff.glb",
    voiceId: "",
}


const airport_laura: AIPersonaType = {
    personaTypeName: "AIRPORT_LAURA",
    nameEndKorean: "와",
    title: "신속한 Laura",
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",
    colors: ["#ffdbef", "#ffdbef"],
    defaultAIName: "Laura",
    defaultAvatarUrl: "https://models.readyplayer.me/64115e1737dc29db74636699.glb",
    voiceId: "",
}


const restaurant_mike: AIPersonaType = {
    personaTypeName: "RESTAURANT_MIKE",
    nameEndKorean: "와",
    title: "센스있는 Mike",
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",
    colors: ["#ffdbef", "#ffdbef"],
    defaultAIName: "Mike",
    defaultAvatarUrl: "https://models.readyplayer.me/63f5a6339233b3995d6d187e.glb",
    voiceId: "",
}


const hospital_susan: AIPersonaType = {
    personaTypeName: "HOSPITAL_SUSAN",
    nameEndKorean: "과",
    title: "전문적인 Susan",
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",
    colors: ["#ffdbef", "#ffdbef"],
    defaultAIName: "Susan",
    defaultAvatarUrl: "https://models.readyplayer.me/63f710ee9233b3995d6e3edc.glb",
    voiceId: "",
}


const interview_tom: AIPersonaType = {
    personaTypeName: "INTERVIEW_TOM",
    nameEndKorean: "과",
    title: "철저한 Tom",
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",
    colors: ["#ffdbef", "#ffdbef"],
    defaultAIName: "Tom",
    defaultAvatarUrl: "https://models.readyplayer.me/6411976937dc29db7463b4ee.glb",
    voiceId: "",
}


const work_james: AIPersonaType = {
    personaTypeName: "WORK_JAMES",
    nameEndKorean: "와",
    title: "똑똑한 James",
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",
    colors: ["#ffdbef", "#ffdbef"],
    defaultAIName: "James",
    defaultAvatarUrl: "https://models.readyplayer.me/63db6c279b552e12bccc5ab3.glb",
    voiceId: "",
}

const work_anna: AIPersonaType = {
    personaTypeName: "WORK_ANNA",
    nameEndKorean: "와",
    title: "꼼꼼한 Anna",
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",
    colors: ["#ffdbef", "#ffdbef"],
    defaultAIName: "Anna",
    defaultAvatarUrl: "https://models.readyplayer.me/6411635337dc29db74636cf1.glb",
    voiceId: "",
}


type SimulationScene = 'DAILY' | 'THEATER' | 'HANGANG' | 'GYM' | 'AIRPORT' | 'HOTEL' | 'RESTAURANT' | 'TOURISM' | 'HOSPITAL' | 'NATIVE_FRIEND' | 'CAMPUS' | 'INTERVIEW' | 'MEETING_ROOM' | 'ONLINE_MEETING'

// Static, pre-made content that we seed into the DB
type SimulationScenario = {
    id: string

    // Type of persona => AIPersonaType
    simulationSceneId: string
    simulationScene: SimulationScene

    /**
     * 
     * 각 시나리오에는 AI 가 한명 씩 있다. Scene
     * AIPersonaType은 우리가 AI 쪽에서 미리 만들어 놓은 AI를 뜻하며
     * 이는 AIPersona와 다른 이유는
     * AIPersona는 각 유저마다의 AIPersonaType의 일환을 트래킹 하기 위함이다
     *  각 유저에게 우리는 AIPersonaType의 "복사본"을 제공하며
     *  각 유저는 앱을 사용하면서 AI와의 개인적인 기억이나 경험을 겪게 된다. 이런 부분들을
     *  AIPersona로 트래킹한다.
     * 
     */
    personaTypeName: string
    personaType: AIPersonaType

    scenarioNameEn: string
    scenarioNameKo: string
    scenarioDescription: string

    backgroundImageUrl: string
    color: string

    createdAt: Date
    updatedAt: Date
}

/*
    Restaurant
        - 예약하기
        - 자리 안내받기
        - 주문하기
        - 식사하기
        - 계산하기

    Airport
        - 항공권 발급 받기
        - 입국심사하기
        - 수화물 찾기
        - 호텔행 택시 부르기
        - 버스 정류장 물어보기

    Tourism
        - 티켓 구매하기
        - 사진 요청하기
        - 길 물어보기
        - 운영 시간 물어보기
        - 잃어버린 물건 찾기
    
    Native friend
        - 자기소개하기
        - 인기 관광지 물어보기
        - 현지인 맛집 물어보기
        - 밥 약속 잡기
        - SNS 맞팔하기

    Jane's school
        - 친구 소개 받기
        - 강의 노트 빌리기
        - 강의실 위치 물어보기
        - 수업 내용 물어보기

    Gym
        - 루틴 공유하기
        - 기구 사용법 물어보기
        - 영양 보충하기
        - 다음 약속 잡기

    Interview
        - 첫인사 나누기
        - 학력 얘기하기
        - 경력 얘기하기
        - 장점 내세우기
        - 단점 얘기하는 법
        - 면접관에게 질문하기
    
    Meeting room
        - 회의 목적 말하기
        - 토의 사항 나누기
        - 동료 의견에 찬성하기
        - 나의 의견 덧붙이기
        - 반대 의견 얘기하기
    
    Online meeting
        - 미팅 시간에 늦었을 때
        - 전화 소리가 끊길 때
        - 네트워크가 안 좋을 때
        - 화면 공유하기
*/


const restaurant_reservation: SimulationScenario = {
    id: "restaurant_reservation",
    simulationSceneId: "",
    simulationScene: "RESTAURANT",

    personaTypeName: "Mike",
    personaType: restaurant_mike,

    scenarioNameEn: "Making a reservation",
    scenarioNameKo: "예약하기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/restaurant_reservation.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const restaurant_seated: SimulationScenario = {
    id: "restaurant_seated",
    simulationSceneId: "",
    simulationScene: "RESTAURANT",

    personaTypeName: "Mike",
    personaType: restaurant_mike,

    scenarioNameEn: "Being seated",
    scenarioNameKo: "자리 안내받기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/restaurant_seated.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const restaurant_order: SimulationScenario = {
    id: "restaurant_order",
    simulationSceneId: "",
    simulationScene: "RESTAURANT",

    personaTypeName: "Mike",
    personaType: restaurant_mike,

    scenarioNameEn: "Placing an order",
    scenarioNameKo: "주문하기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/restaurant_order.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const restaurant_eat: SimulationScenario = {
    id: "restaurant_eat",
    simulationSceneId: "",
    simulationScene: "RESTAURANT",

    personaTypeName: "Mike",
    personaType: restaurant_mike,

    scenarioNameEn: "Receiving and enjoying the meal",
    scenarioNameKo: "식사하기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/restaurant_eat.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const restaurant_pay: SimulationScenario = {
    id: "restaurant_pay",
    simulationSceneId: "",
    simulationScene: "RESTAURANT",

    personaTypeName: "Mike",
    personaType: restaurant_mike,

    scenarioNameEn: "Making a payment",
    scenarioNameKo: "계산하기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/restaurant_pay.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const airport_boardingpass: SimulationScenario = {
    id: "airport_boardingpass",
    simulationSceneId: "",
    simulationScene: "AIRPORT",

    personaTypeName: "Laura",
    personaType: airport_laura,

    scenarioNameEn: "Getting a boarding pass",
    scenarioNameKo: "항공권 발급 받기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/airport_boardingpass.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const airport_immigration: SimulationScenario = {
    id: "airport_immigration",
    simulationSceneId: "",
    simulationScene: "AIRPORT",

    personaTypeName: "Laura",
    personaType: airport_laura,

    scenarioNameEn: "Going through immigration",
    scenarioNameKo: "입국심사하기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/airport_immigration.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const airport_baggage: SimulationScenario = {
    id: "airport_baggage",
    simulationSceneId: "",
    simulationScene: "AIRPORT",

    personaTypeName: "Laura",
    personaType: airport_laura,

    scenarioNameEn: "Finding your luggages",
    scenarioNameKo: "수화물 찾기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/airport_baggage.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const airport_taxi: SimulationScenario = {
    id: "airport_taxi",
    simulationSceneId: "",
    simulationScene: "AIRPORT",

    personaTypeName: "Laura",
    personaType: airport_laura,

    scenarioNameEn: "Calling a taxi to the hotel",
    scenarioNameKo: "호텔형 택시 부르기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/airport_taxi.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}


const airport_busstop: SimulationScenario = {
    id: "airport_busstop",
    simulationSceneId: "",
    simulationScene: "AIRPORT",

    personaTypeName: "Laura",
    personaType: airport_laura,

    scenarioNameEn: "Looking for a bus stop",
    scenarioNameKo: "버스 정류장 물어보기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/airport_busstop.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}


const tourism_ticket: SimulationScenario = {
    id: "tourism_ticket",
    simulationSceneId: "",
    simulationScene: "TOURISM",

    personaTypeName: "Sophie",
    personaType: tourism_sophie,

    scenarioNameEn: "Buying the tickets",
    scenarioNameKo: "티켓 구매하기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/tourism_ticket.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const tourism_photo: SimulationScenario = {
    id: "tourism_photo",
    simulationSceneId: "",
    simulationScene: "TOURISM",

    personaTypeName: "Lucas",
    personaType: tourism_lucas,

    scenarioNameEn: "Asking for a photo",
    scenarioNameKo: "사진 요청하기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/tourism_photo.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const tourism_direction: SimulationScenario = {
    id: "tourism_direction",
    simulationSceneId: "",
    simulationScene: "TOURISM",

    personaTypeName: "Sophie",
    personaType: tourism_sophie,

    scenarioNameEn: "Asking for directions",
    scenarioNameKo: "길 물어보기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/tourism_direction.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const tourism_hours: SimulationScenario = {
    id: "tourism_hours",
    simulationSceneId: "",
    simulationScene: "TOURISM",

    personaTypeName: "Sophie",
    personaType: tourism_sophie,

    scenarioNameEn: "Asking for hours of operation",
    scenarioNameKo: "운영 시간 물어보기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/tourism_hours.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const tourism_lostandfound: SimulationScenario = {
    id: "tourism_lostandfound",
    simulationSceneId: "",
    simulationScene: "TOURISM",

    personaTypeName: "Sophie",
    personaType: tourism_sophie,

    scenarioNameEn: "Finding lost items",
    scenarioNameKo: "잃어버린 물건 찾기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/tourism_lostandfound.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}


const native_introduce: SimulationScenario = {
    id: "native_introduce",
    simulationSceneId: "",
    simulationScene: "NATIVE_FRIEND",

    personaTypeName: "Lucas",
    personaType: tourism_lucas,

    scenarioNameEn: "Introducing yourself",
    scenarioNameKo: "자기소개하기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/restaurant_pay.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const native_tourism: SimulationScenario = {
    id: "native_tourism",
    simulationSceneId: "",
    simulationScene: "NATIVE_FRIEND",

    personaTypeName: "Lucas",
    personaType: tourism_lucas,

    scenarioNameEn: "Asking about tourist attractions",
    scenarioNameKo: "인기 관광지 물어보기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const native_food: SimulationScenario = {
    id: "native_food",
    simulationSceneId: "",
    simulationScene: "NATIVE_FRIEND",

    personaTypeName: "Lucas",
    personaType: tourism_lucas,

    scenarioNameEn: "Asking for must-eat restaurants",
    scenarioNameKo: "현지인 맛집 물어보기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/native_food.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const native_lunch: SimulationScenario = {
    id: "native_lunch",
    simulationSceneId: "",
    simulationScene: "NATIVE_FRIEND",

    personaTypeName: "Lucas",
    personaType: tourism_lucas,

    scenarioNameEn: "Asking to make plans",
    scenarioNameKo: "밥 약속 잡기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/native_lunch.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const native_socialmedia: SimulationScenario = {
    id: "native_socialmedia",
    simulationSceneId: "",
    simulationScene: "NATIVE_FRIEND",

    personaTypeName: "Lucas",
    personaType: tourism_lucas,

    scenarioNameEn: "Connecting on social media",
    scenarioNameKo: "SNS 맞팔하기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/native_socialmedia.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const school_introducefriend: SimulationScenario = {
    id: "school_introducefriend",
    simulationSceneId: "",
    simulationScene: "DAILY",

    personaTypeName: "Jane",
    personaType: metabuddy_jane,

    scenarioNameEn: "Being introduced to a new friend",
    scenarioNameKo: "친구 소개 받기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/school_introducefriend.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const school_note: SimulationScenario = {
    id: "school_note",
    simulationSceneId: "",
    simulationScene: "DAILY",

    personaTypeName: "Jane",
    personaType: metabuddy_jane,

    scenarioNameEn: "Asking for lecture notes",
    scenarioNameKo: "강의 노트 빌리기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/school_note.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const school_lectureroom: SimulationScenario = {
    id: "school_lectureroom",
    simulationSceneId: "",
    simulationScene: "DAILY",

    personaTypeName: "Jane",
    personaType: metabuddy_jane,

    scenarioNameEn: "Asking for classroom location",
    scenarioNameKo: "강의실 위치 물어보기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/school_lectureroom.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const school_lecture: SimulationScenario = {
    id: "school_lecture",
    simulationSceneId: "",
    simulationScene: "DAILY",

    personaTypeName: "Jane",
    personaType: metabuddy_jane,

    scenarioNameEn: "Asking about the lecture content",
    scenarioNameKo: "수업 내용 물어보기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/school_lecture.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const gym_routine: SimulationScenario = {
    id: "gym_routine",
    simulationSceneId: "",
    simulationScene: "GYM",

    personaTypeName: "Ryan",
    personaType: metabuddy_ryan,

    scenarioNameEn: "Sharing your workout routine",
    scenarioNameKo: "루틴 공유하기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/gym_routine.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const gym_machine: SimulationScenario = {
    id: "gym_machine",
    simulationSceneId: "",
    simulationScene: "GYM",

    personaTypeName: "Ryan",
    personaType: metabuddy_ryan,

    scenarioNameEn: "Asking how to use a machine",
    scenarioNameKo: "기구 사용법 물어보기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/gym_machine.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const gym_eat: SimulationScenario = {
    id: "gym_eat",
    simulationSceneId: "",
    simulationScene: "GYM",

    personaTypeName: "Ryan",
    personaType: metabuddy_ryan,

    scenarioNameEn: "Getting food after the workout",
    scenarioNameKo: "영양 보충하기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/gym_eat.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const gym_nextplan: SimulationScenario = {
    id: "gym_nextplan",
    simulationSceneId: "",
    simulationScene: "GYM",

    personaTypeName: "Ryan",
    personaType: metabuddy_ryan,

    scenarioNameEn: "Scheduling your next workout",
    scenarioNameKo: "다음 약속 잡기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/gym_nextplan.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}


const interview_hello: SimulationScenario = {
    id: "interview_hello",
    simulationSceneId: "",
    simulationScene: "INTERVIEW",

    personaTypeName: "Tom",
    personaType: interview_tom,

    scenarioNameEn: "Introducing yourself",
    scenarioNameKo: "첫인사 나누기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/interview_hello.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const interview_education: SimulationScenario = {
    id: "interview_education",
    simulationSceneId: "",
    simulationScene: "INTERVIEW",

    personaTypeName: "Tom",
    personaType: interview_tom,

    scenarioNameEn: "Talking about your education",
    scenarioNameKo: "학력 얘기하기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/interview_education.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const interview_experience: SimulationScenario = {
    id: "interview_experience",
    simulationSceneId: "",
    simulationScene: "INTERVIEW",

    personaTypeName: "Tom",
    personaType: interview_tom,

    scenarioNameEn: "Talking about your experience",
    scenarioNameKo: "경력 얘기하기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/interview_experience.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const interview_strengths: SimulationScenario = {
    id: "interview_strengths",
    simulationSceneId: "",
    simulationScene: "INTERVIEW",

    personaTypeName: "Tom",
    personaType: interview_tom,

    scenarioNameEn: "Talking about your strengths",
    scenarioNameKo: "장점 내세우기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/interview_strengths.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const interview_weaknesses: SimulationScenario = {
    id: "interview_weaknesses",
    simulationSceneId: "",
    simulationScene: "INTERVIEW",

    personaTypeName: "Tom",
    personaType: interview_tom,

    scenarioNameEn: "Talking about your weaknesses",
    scenarioNameKo: "단점 얘기하는 법",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/interview_weaknesses.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const interview_questions: SimulationScenario = {
    id: "interview_questions",
    simulationSceneId: "",
    simulationScene: "INTERVIEW",

    personaTypeName: "Tom",
    personaType: interview_tom,

    scenarioNameEn: "Asking questions to the interviewer",
    scenarioNameKo: "면접관에게 질문하기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/interview_questions.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const meetingroom_purpose: SimulationScenario = {
    id: "meetingroom_purpose",
    simulationSceneId: "",
    simulationScene: "MEETING_ROOM",

    personaTypeName: "James",
    personaType: work_james,

    scenarioNameEn: "Stating the purpose of the meeting",
    scenarioNameKo: "회의 목적 말하기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/meetingroom_purpose.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}


const meetingroom_discussion: SimulationScenario = {
    id: "meetingroom_discussion",
    simulationSceneId: "",
    simulationScene: "MEETING_ROOM",

    personaTypeName: "James",
    personaType: work_james,

    scenarioNameEn: "Sharing discussion points",
    scenarioNameKo: "토의 사항 나누기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/meetingroom_discussion.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const meetingroom_agree: SimulationScenario = {
    id: "meetingroom_agree",
    simulationSceneId: "",
    simulationScene: "MEETING_ROOM",

    personaTypeName: "James",
    personaType: work_james,

    scenarioNameEn: "Agreeing with a colleague",
    scenarioNameKo: "동료 의견에 찬성하기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/meetingroom_agree.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const meetingroom_opinion: SimulationScenario = {
    id: "meetingroom_opinion",
    simulationSceneId: "",
    simulationScene: "MEETING_ROOM",

    personaTypeName: "James",
    personaType: work_james,

    scenarioNameEn: "Adding your opinion",
    scenarioNameKo: "나의 의견 덧붙이기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/meetingroom_opinion.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const meetingroom_disagree: SimulationScenario = {
    id: "meetingroom_disagree",
    simulationSceneId: "",
    simulationScene: "MEETING_ROOM",

    personaTypeName: "James",
    personaType: work_james,

    scenarioNameEn: "Disagreeing with a colleague",
    scenarioNameKo: "반대 의견 얘기하기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/meetingroom_disagree.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}


const onlinemeeting_late: SimulationScenario = {
    id: "onlinemeeting_late",
    simulationSceneId: "",
    simulationScene: "ONLINE_MEETING",

    personaTypeName: "James",
    personaType: work_james,

    scenarioNameEn: "Being late for a meeting",
    scenarioNameKo: "미팅 시간에 늦었을 때",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/onlinemeeting_late.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}


const onlinemeeting_sound: SimulationScenario = {
    id: "onlinemeeting_sound",
    simulationSceneId: "",
    simulationScene: "ONLINE_MEETING",

    personaTypeName: "James",
    personaType: work_james,

    scenarioNameEn: "When the voice is cutting out",
    scenarioNameKo: "전화 소리가 끊길 때",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/onlinemeeting_sound.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const onlinemeeting_connection: SimulationScenario = {
    id: "onlinemeeting_connection",
    simulationSceneId: "",
    simulationScene: "ONLINE_MEETING",

    personaTypeName: "James",
    personaType: work_james,

    scenarioNameEn: "Having a poor network connection",
    scenarioNameKo: "네트워크가 안 좋을 때",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/onlinemeeting_connection.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}

const onlinemeeting_screenshare: SimulationScenario = {
    id: "onlinemeeting_screenshare",
    simulationSceneId: "",
    simulationScene: "ONLINE_MEETING",

    personaTypeName: "James",
    personaType: work_james,

    scenarioNameEn: "Sharing your screen",
    scenarioNameKo: "화면 공유하기",
    scenarioDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean fringilla auctor ultrices.",

    backgroundImageUrl: "https://metabuddy-assets.s3.ap-northeast-2.amazonaws.com/scenario_images/onlinemeeting_screenshare.png",
    color: "#ffdbef",
    createdAt: new Date(),
    updatedAt: new Date()
}