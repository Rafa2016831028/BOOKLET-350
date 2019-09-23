import * as React from "react";
import styled from "styled-components";
import Hero from '../components/Hero'
import Banner from '../components/Banner'
import {Link} from "react-router-dom"
import Services from "../components/Services"
import ChildDiv from "../components/ChildDiv"
import RecipeReviewCard from "../components/SingleBookCart"
import axios from 'axios';
import MainDiv from '../components/MainDiv'

class Home extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            bookList : [ ],
        }
    }
    render() {
        const  {bookList } = this.state
        return (
            <React.Fragment>
                <MainDiv>
                    <Hero >
                        <Banner title="BOOKLET" subtitle="Welcome to the world of desire">
                            <Link to="/books" className="btn-primary">Get Them</Link>
                        </Banner>
                    </Hero>

                    <h3>Books List: </h3>

                    <ChildDiv>
                        {bookList.map(book => (
                            <RecipeReviewCard key={book.id} book={book}/>
                        ))}
                        {/*<RecipeReviewCard book = {bookList}></RecipeReviewCard>*/}
                    </ChildDiv>
                    <Services/>
                </MainDiv>

            </React.Fragment>
        )
    }

    componentDidMount() {
        axios.get('http://localhost:8000/books/')
            .then(response => {
                console.log(response.data)
                this.setState({
                    bookList : response.data,
            
                })
            }).catch(error => {
        
        })
    }
}
export default Home
