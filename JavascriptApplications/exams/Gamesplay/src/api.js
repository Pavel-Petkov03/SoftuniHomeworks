const host = 'http://localhost:3030'

export const endpoints = {
    register: `${host}/users/register`,
    login: `${host}/users/login`,
    logout: `${host}/users/logout`,
    catalog: `${host}/data/games?sortBy=_createdOn%20desc&distinct=category`,
    allGames: `${host}/data/games?sortBy=_createdOn%20desc`,
    create: `${host}/data/games`,
    details: (id) => `${host}/data/games/${id}`,
    delete: (id) => `${host}/data/games/${id}`,
    comments: (id) => `${host}/data/comments?where=gameId%3D%22${id}%22`,
    postComments: `${host}/data/comments`
};

