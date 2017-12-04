import {
    FETCH_EXAMENES,
    FETCH_EXAMEN,
    DELETE_EXAMEN,
    CREATE_EXAMEN,
    UPDATE_EXAMEN
} from './02_types';

import axios from 'axios';

const ROOT_URL = '/api/';
const FORMAT = 'format=json';

export function fetchExamenes() {
    return function (dispatch) {
        const SUB_URL = 'examenes/';
        const FULL_URL = `${ROOT_URL}${SUB_URL}?${FORMAT}`;
        axios.get(FULL_URL)
            .then(response => {
                    dispatch({type: FETCH_EXAMENES, payload: response})
                }
            ).catch(function (error) {

        })
    }
}

export function fetchExamenesxParametro(parametro, callback = null, callback_error = null) {
    return function (dispatch) {
        const SUB_URL = `examenes/buscar_x_parametro?parametro=${parametro}`;
        const FULL_URL = `${ROOT_URL}${SUB_URL}&${FORMAT}`;
        axios.get(FULL_URL)
            .then(response => {
                dispatch({type: FETCH_EXAMENES, payload: response});
                if (callback) {
                    callback(response.data)
                }
            }).catch(error => {
            if (callback_error) {
                callback_error(error)
            }
        });
    }
}

export function refreshExamen(examen) {
    return {
        type: FETCH_EXAMEN,
        payload: examen
    }
}

export function deleteExamen(id) {
    return {
        type: DELETE_EXAMEN,
        payload: id
    }
}

export function fetchExamen(id) {
    return function (dispatch) {
        const SUB_URL = `examenes/${id}/`;
        const FULL_URL = `${ROOT_URL}${SUB_URL}?${FORMAT}`;
        axios.get(FULL_URL)
            .then(response => {

                    dispatch({type: FETCH_EXAMEN, payload: response})
                }
            ).catch(function (error) {

        })
    }
}


export function crearExamen(values, callback) {
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    axios.defaults.xsrfCookieName = "csrftoken";
    const request = axios.post(`${ROOT_URL}examenes/`, values).then(() => callback()).catch(error => {
        console.log(error)
    });
    return {
        type: CREATE_EXAMEN,
        payload: request
    };
}

export function updateExamen(id, values, callback) {
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    axios.defaults.xsrfCookieName = "csrftoken";
    const request = axios.put(`${ROOT_URL}examenes/${id}/`, values).then(() => callback()).catch(error => {
        console.log(error)
    });
    return {
        type: UPDATE_EXAMEN,
        payload: request
    };
}