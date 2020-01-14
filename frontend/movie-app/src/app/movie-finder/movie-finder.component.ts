import { Component, OnInit } from '@angular/core';
import { MovieService } from './movie-finder.service.component';
import { IMovie } from './movie.model';
import { HttpErrorResponse, HttpResponse } from '@angular/common/http';

@Component({
  selector: 'app-movie-finder',
  templateUrl: './movie-finder.component.html',
  styleUrls: ['./movie-finder.component.scss']
})
export class MovieFinderComponent implements OnInit {

  movies: IMovie[];
  message: any;
  search = '';
  filterBy = 'primaryTitle';
  page = 0;
  totalItems = 0;

  constructor(
    private movieService: MovieService
  ) { }

  ngOnInit() {
    this.loadMovies();
  }

  loadMovies() {
    this.movieService
    .query({
      filterBy: this.filterBy,
      search: this.search,
      page: this.page})
    .subscribe(
      (res: HttpResponse<IMovie[]>) => this.validateSearch(this.movies = res.body),
      (res: HttpErrorResponse) => console.log(res.message)
    );
  }


  validateSearch(result) {
    this.movies = result["data"];
    this.totalItems = result["totalItems"];
  }

  searchChanged() {
    this.page = 0;
    this.loadMovies();
  }

  pageChanged(page) {
    this.page = page - 1;
    this.loadMovies();
  }
 
}
