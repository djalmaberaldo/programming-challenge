import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { IMovie, IName } from './movie.model';
import { SERVER_API_URL } from '../app.constants';

type EntityArrayResponseType = HttpResponse<IMovie[]>;

@Injectable({ providedIn: 'root' })
export class MovieService {
  public resourceUrl = SERVER_API_URL + '/movies';

  constructor(protected http: HttpClient) {}

  query(req?: any): Observable<EntityArrayResponseType> {
    return this.http
      .get<IMovie[]>(this.resourceUrl, { params: req, observe: 'response' });
  }

  findNames(req?: any): Observable<EntityArrayResponseType> {
    return this.http
      .get<IName[]>(this.resourceUrl + '/names', { params: req, observe: 'response' });
  }

  findByYear(req?: any): Observable<EntityArrayResponseType> {
    return this.http
      .get<IMovie[]>(this.resourceUrl + '/by-year', { params: req, observe: 'response' });
  }
}
