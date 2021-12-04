const host = 'http://localhost:3030'; 
export const endpoints = {
    register: `${host}/users/register`,
    login: `${host}/users/login`,
    logout: `${host}/users/logout`,
    catalog: `${host}/data/albums?sortBy=_createdOn%20desc&distinct=name`,
    create: `${host}/data/albums`,
    details: (id) => `${host}/data/albums/${id}`,
    delete: (id) => `${host}/data/albums/${id}`,
    search: (query) => `${host}/data/albums?where=name%20LIKE%20%22${query}%22`
};