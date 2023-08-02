import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-side-panel',
  templateUrl: './side-panel.component.html',
  styleUrls: ['./side-panel.component.css']
})
export class SidePanelComponent {

  @Input() sideNavStatus:boolean = false;

  list = [
    {
      number: 1,
      name: 'md5 Hashing'
    },
    {
      number: 2,
      name: 'Tracking'
    }
  ]

}
