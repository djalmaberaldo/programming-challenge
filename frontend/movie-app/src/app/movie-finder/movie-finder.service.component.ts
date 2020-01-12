import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { IMovie } from './movie.model';
import { SERVER_API_URL } from '../app.constants';

type EntityArrayResponseType = HttpResponse<IMovie[]>;

@Injectable({ providedIn: 'root' })
export class MovieService {
  public resourceUrl = SERVER_API_URL + '/titles';

  constructor(protected http: HttpClient) {}

  query(req?: any): Observable<EntityArrayResponseType> {
    return this.http
      .get<IMovie[]>(this.resourceUrl, { params: req, observe: 'response' });
  }

}
