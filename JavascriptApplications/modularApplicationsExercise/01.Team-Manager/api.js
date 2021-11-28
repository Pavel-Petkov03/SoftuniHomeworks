const host = "http://localhost:3030"


export const endpoints = {
    teams : `${host}/data/teams`,
    myProfile : (ownerId) => `${host}/data/members?where=_ownerId%3D%22${ownerId}%22%20AND%20status%3D%22member%22&load=team%3DteamId%3Ateams`,
    teamsForParticularMember : (ownerId) => `${host}/data/teams/?where=_ownerId%3D%22${ownerId}%22%20`,
    allParticipantsInTeam : (id) => `${host}/data/teams?where=teamId%3D%22${id}%22%20AND%20status%3D%22member%22&load=team%3DteamId%3Ateams`,
    currentTeam : (teamId) =>  `${host}/data/teams/${teamId}`,
    currentMember : (userId) => `${host}/data/members/${userId}`,
    allPeopleInAllTeams : `${host}/data/members`,
    register : `${host}/users/register`,
    login : `${host}/users/login`,
    queryMembersByKey : (teamId , key) => `${host}/data/members?where=teamId%3D%22${teamId}%22%20AND%20status%3D%22${key}%22&load=user%3D_ownerId%3Ausers`,
    findPersonInParticularTeam : (teamId , userId) => `${host}/data/members?where=teamId%3D%22${teamId}%22%20AND%20_ownerId%3D%22${userId}%22`
}


