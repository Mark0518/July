import { Component, OnInit, AfterViewInit } from '@angular/core';
import { TdMediaService } from '@covalent/core';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.css']
})

export class AdminComponent implements OnInit, AfterViewInit {

  constructor(public media: TdMediaService) { }

  ngOnInit() { }

  ngAfterViewInit(): void {
    this.media.broadcast();
  }
}