def query_prs_from_user(user: str) -> str:

    return '''
        query {
            user(login: "%s") {
                repositories(first: 100) {
                    nodes {
                        sshUrl
                        name
                        open: pullRequests(first: 100, states: OPEN) {
                            nodes {
                                number
                                branch: headRefName
                            }
                        }
                        merged: pullRequests(first: 100, states: MERGED) {
                            nodes {
                                number
                            }
                        }
                        closed: pullRequests(first: 100, states: CLOSED) {
                            nodes {
                                number
                            }
                        }
                    }
                }
            }
        }
    ''' % user
