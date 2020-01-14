import { Component, OnInit } from '@angular/core';
import { MovieService } from './movie-finder.service.component';
import { IMovie, IName } from './movie.model';
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
  movieNames = [];
  year = '';

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

  loadMoviesByYear() {
    this.movieService
    .findByYear({year: this.year, page: this.page})
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

  yearSearchChanged() {
    this.page = 0;
    this.loadMoviesByYear();
  }

  pageChanged(page) {
    this.page = page - 1;
    this.movieNames = [];
    if (this.year){
      this.loadMoviesByYear();
    } else {
      this.loadMovies();
    }
  }

  findName(identifier) {
    this.movieService
      .findNames({
        tconst: identifier
      }).subscribe(
        (res: HttpResponse<IName[]>) => this.movieNames[identifier] = this.checkNameResult(res.body['data']),
        (res: HttpErrorResponse) => console.log(res.message)
      );
  }

  checkNameResult(result) {
    if (Array.isArray(result) && result.length) {
      return result.map(x => x.primaryName).join(',');
    } else {
      return 'Result not found';
    }
  }

  adjustNames(id) {
    return this.movieNames[id];
  }
}

