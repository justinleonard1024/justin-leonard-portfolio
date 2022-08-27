/********************************
 * Custom Game Show
 * FormMainSettings.Designer.cs
 * Created by Justin Leonard
********************************/

namespace CustomGameShow
{
    partial class FormMainSettings
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(FormMainSettings));
            this.buttonExit = new System.Windows.Forms.Button();
            this.labelTitle = new System.Windows.Forms.Label();
            this.listBoxText = new System.Windows.Forms.ListBox();
            this.textBoxText = new System.Windows.Forms.TextBox();
            this.listBoxColor = new System.Windows.Forms.ListBox();
            this.buttonColor = new System.Windows.Forms.Button();
            this.pictureBoxColor = new System.Windows.Forms.PictureBox();
            this.listBoxType = new System.Windows.Forms.ListBox();
            this.comboBoxType = new System.Windows.Forms.ComboBox();
            this.buttonSaveAll = new System.Windows.Forms.Button();
            this.buttonSaveText = new System.Windows.Forms.Button();
            this.buttonSaveColor = new System.Windows.Forms.Button();
            this.buttonSaveType = new System.Windows.Forms.Button();
            this.colorDialogMain = new System.Windows.Forms.ColorDialog();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxColor)).BeginInit();
            this.SuspendLayout();
            // 
            // buttonExit
            // 
            this.buttonExit.BackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonExit.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("buttonExit.BackgroundImage")));
            this.buttonExit.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.buttonExit.Cursor = System.Windows.Forms.Cursors.Hand;
            this.buttonExit.FlatAppearance.BorderColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonExit.FlatAppearance.BorderSize = 0;
            this.buttonExit.FlatAppearance.CheckedBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonExit.FlatAppearance.MouseDownBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonExit.FlatAppearance.MouseOverBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonExit.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonExit.Font = new System.Drawing.Font("Arial", 36F, System.Drawing.FontStyle.Bold);
            this.buttonExit.Location = new System.Drawing.Point(1002, 961);
            this.buttonExit.Name = "buttonExit";
            this.buttonExit.Size = new System.Drawing.Size(468, 75);
            this.buttonExit.TabIndex = 0;
            this.buttonExit.TabStop = false;
            this.buttonExit.Text = "Exit";
            this.buttonExit.UseVisualStyleBackColor = false;
            this.buttonExit.Click += new System.EventHandler(this.buttonExit_Click);
            // 
            // labelTitle
            // 
            this.labelTitle.AutoSize = true;
            this.labelTitle.Font = new System.Drawing.Font("Arial Black", 72F, System.Drawing.FontStyle.Bold);
            this.labelTitle.ForeColor = System.Drawing.SystemColors.ControlText;
            this.labelTitle.Location = new System.Drawing.Point(719, 3);
            this.labelTitle.Name = "labelTitle";
            this.labelTitle.Size = new System.Drawing.Size(495, 136);
            this.labelTitle.TabIndex = 0;
            this.labelTitle.Text = "Settings";
            // 
            // listBoxText
            // 
            this.listBoxText.BackColor = System.Drawing.SystemColors.Control;
            this.listBoxText.Font = new System.Drawing.Font("Arial", 36F, System.Drawing.FontStyle.Bold);
            this.listBoxText.FormattingEnabled = true;
            this.listBoxText.ItemHeight = 56;
            this.listBoxText.Items.AddRange(new object[] {
            "Contestant Name 1",
            "Contestant Name 2",
            "Contestant Name 3"});
            this.listBoxText.Location = new System.Drawing.Point(32, 148);
            this.listBoxText.Name = "listBoxText";
            this.listBoxText.Size = new System.Drawing.Size(582, 620);
            this.listBoxText.TabIndex = 0;
            this.listBoxText.TabStop = false;
            this.listBoxText.SelectedIndexChanged += new System.EventHandler(this.listBoxText_SelectedIndexChanged);
            // 
            // textBoxText
            // 
            this.textBoxText.BackColor = System.Drawing.SystemColors.Control;
            this.textBoxText.Font = new System.Drawing.Font("Arial", 27.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.textBoxText.Location = new System.Drawing.Point(32, 787);
            this.textBoxText.Name = "textBoxText";
            this.textBoxText.Size = new System.Drawing.Size(582, 50);
            this.textBoxText.TabIndex = 0;
            this.textBoxText.TabStop = false;
            // 
            // listBoxColor
            // 
            this.listBoxColor.BackColor = System.Drawing.SystemColors.Control;
            this.listBoxColor.Font = new System.Drawing.Font("Arial", 36F, System.Drawing.FontStyle.Bold);
            this.listBoxColor.FormattingEnabled = true;
            this.listBoxColor.ItemHeight = 56;
            this.listBoxColor.Items.AddRange(new object[] {
            "Game Board Color",
            "Contestant Color 1",
            "Contestant Color 2",
            "Contestant Color 3",
            "Category Color 1",
            "Category Color 2",
            "Category Color 3",
            "Category Color 4",
            "Category Color 5",
            "Category Color 6",
            "Category Color 7",
            "Category Color 8",
            "Category Color 9",
            "Category Color 10"});
            this.listBoxColor.Location = new System.Drawing.Point(669, 148);
            this.listBoxColor.Name = "listBoxColor";
            this.listBoxColor.Size = new System.Drawing.Size(582, 620);
            this.listBoxColor.TabIndex = 0;
            this.listBoxColor.TabStop = false;
            this.listBoxColor.SelectedIndexChanged += new System.EventHandler(this.listBoxColor_SelectedIndexChanged);
            // 
            // buttonColor
            // 
            this.buttonColor.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("buttonColor.BackgroundImage")));
            this.buttonColor.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.buttonColor.Cursor = System.Windows.Forms.Cursors.Hand;
            this.buttonColor.FlatAppearance.BorderColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonColor.FlatAppearance.BorderSize = 0;
            this.buttonColor.FlatAppearance.CheckedBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonColor.FlatAppearance.MouseDownBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonColor.FlatAppearance.MouseOverBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonColor.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonColor.Font = new System.Drawing.Font("Arial", 27.75F, System.Drawing.FontStyle.Bold);
            this.buttonColor.Location = new System.Drawing.Point(669, 787);
            this.buttonColor.Name = "buttonColor";
            this.buttonColor.Size = new System.Drawing.Size(280, 50);
            this.buttonColor.TabIndex = 0;
            this.buttonColor.TabStop = false;
            this.buttonColor.Text = "Select Color";
            this.buttonColor.UseVisualStyleBackColor = true;
            this.buttonColor.Click += new System.EventHandler(this.buttonColor_Click);
            // 
            // pictureBoxColor
            // 
            this.pictureBoxColor.BackColor = System.Drawing.Color.Transparent;
            this.pictureBoxColor.Location = new System.Drawing.Point(971, 787);
            this.pictureBoxColor.Name = "pictureBoxColor";
            this.pictureBoxColor.Size = new System.Drawing.Size(280, 50);
            this.pictureBoxColor.TabIndex = 0;
            this.pictureBoxColor.TabStop = false;
            // 
            // listBoxType
            // 
            this.listBoxType.BackColor = System.Drawing.SystemColors.Control;
            this.listBoxType.Font = new System.Drawing.Font("Arial", 36F, System.Drawing.FontStyle.Bold);
            this.listBoxType.FormattingEnabled = true;
            this.listBoxType.ItemHeight = 56;
            this.listBoxType.Items.AddRange(new object[] {
            "Media Type 1 1",
            "Media Type 1 2",
            "Media Type 1 3",
            "Media Type 1 4",
            "Media Type 1 5",
            "Media Type 1 6",
            "Media Type 1 7",
            "Media Type 1 8",
            "Media Type 1 9",
            "Media Type 1 10",
            "Media Type 1 11",
            "Media Type 1 12",
            "Media Type 2 1",
            "Media Type 2 2",
            "Media Type 2 3",
            "Media Type 2 4",
            "Media Type 2 5",
            "Media Type 2 6",
            "Media Type 2 7",
            "Media Type 2 8",
            "Media Type 2 9",
            "Media Type 2 10",
            "Media Type 2 11",
            "Media Type 2 12",
            "Media Type 3 1",
            "Media Type 3 2",
            "Media Type 3 3",
            "Media Type 3 4",
            "Media Type 3 5",
            "Media Type 3 6",
            "Media Type 3 7",
            "Media Type 3 8",
            "Media Type 3 9",
            "Media Type 3 10",
            "Media Type 3 11",
            "Media Type 3 12",
            "Media Type 4 1",
            "Media Type 4 2",
            "Media Type 4 3",
            "Media Type 4 4",
            "Media Type 4 5",
            "Media Type 4 6",
            "Media Type 4 7",
            "Media Type 4 8",
            "Media Type 4 9",
            "Media Type 4 10",
            "Media Type 4 11",
            "Media Type 4 12",
            "Media Type 5 1",
            "Media Type 5 2",
            "Media Type 5 3",
            "Media Type 5 4",
            "Media Type 5 5",
            "Media Type 5 6",
            "Media Type 5 7",
            "Media Type 5 8",
            "Media Type 5 9",
            "Media Type 5 10",
            "Media Type 5 11",
            "Media Type 5 12",
            "Media Type 6 1",
            "Media Type 6 2",
            "Media Type 6 3",
            "Media Type 6 4",
            "Media Type 6 5",
            "Media Type 6 6",
            "Media Type 6 7",
            "Media Type 6 8",
            "Media Type 6 9",
            "Media Type 6 10",
            "Media Type 6 11",
            "Media Type 6 12",
            "Media Type 7 1",
            "Media Type 7 2",
            "Media Type 7 3",
            "Media Type 7 4",
            "Media Type 7 5",
            "Media Type 7 6",
            "Media Type 7 7",
            "Media Type 7 8",
            "Media Type 7 9",
            "Media Type 7 10",
            "Media Type 7 11",
            "Media Type 7 12",
            "Media Type 8 1",
            "Media Type 8 2",
            "Media Type 8 3",
            "Media Type 8 4",
            "Media Type 8 5",
            "Media Type 8 6",
            "Media Type 8 7",
            "Media Type 8 8",
            "Media Type 8 9",
            "Media Type 8 10",
            "Media Type 8 11",
            "Media Type 8 12",
            "Media Type 9 1",
            "Media Type 9 2",
            "Media Type 9 3",
            "Media Type 9 4",
            "Media Type 9 5",
            "Media Type 9 6",
            "Media Type 9 7",
            "Media Type 9 8",
            "Media Type 9 9",
            "Media Type 9 10",
            "Media Type 9 11",
            "Media Type 9 12",
            "Media Type 10 1",
            "Media Type 10 2",
            "Media Type 10 3",
            "Media Type 10 4",
            "Media Type 10 5",
            "Media Type 10 6",
            "Media Type 10 7",
            "Media Type 10 8",
            "Media Type 10 9",
            "Media Type 10 10",
            "Media Type 10 11",
            "Media Type 10 12"});
            this.listBoxType.Location = new System.Drawing.Point(1306, 148);
            this.listBoxType.Name = "listBoxType";
            this.listBoxType.Size = new System.Drawing.Size(582, 620);
            this.listBoxType.TabIndex = 0;
            this.listBoxType.TabStop = false;
            this.listBoxType.SelectedIndexChanged += new System.EventHandler(this.listBoxType_SelectedIndexChanged);
            // 
            // comboBoxType
            // 
            this.comboBoxType.BackColor = System.Drawing.SystemColors.Control;
            this.comboBoxType.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.comboBoxType.Font = new System.Drawing.Font("Arial", 27.75F, System.Drawing.FontStyle.Bold);
            this.comboBoxType.FormattingEnabled = true;
            this.comboBoxType.Items.AddRange(new object[] {
            "ImageImage",
            "ImageVideoImageImage",
            "ImageVideoImageVideo",
            "VideoImageImage",
            "VideoImageVideo"});
            this.comboBoxType.Location = new System.Drawing.Point(1306, 787);
            this.comboBoxType.Name = "comboBoxType";
            this.comboBoxType.Size = new System.Drawing.Size(582, 52);
            this.comboBoxType.TabIndex = 0;
            this.comboBoxType.TabStop = false;
            // 
            // buttonSaveAll
            // 
            this.buttonSaveAll.BackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonSaveAll.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("buttonSaveAll.BackgroundImage")));
            this.buttonSaveAll.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.buttonSaveAll.Cursor = System.Windows.Forms.Cursors.Hand;
            this.buttonSaveAll.FlatAppearance.BorderColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonSaveAll.FlatAppearance.BorderSize = 0;
            this.buttonSaveAll.FlatAppearance.CheckedBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonSaveAll.FlatAppearance.MouseDownBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonSaveAll.FlatAppearance.MouseOverBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonSaveAll.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonSaveAll.Font = new System.Drawing.Font("Arial", 36F, System.Drawing.FontStyle.Bold);
            this.buttonSaveAll.Location = new System.Drawing.Point(450, 961);
            this.buttonSaveAll.Name = "buttonSaveAll";
            this.buttonSaveAll.Size = new System.Drawing.Size(468, 75);
            this.buttonSaveAll.TabIndex = 0;
            this.buttonSaveAll.TabStop = false;
            this.buttonSaveAll.Text = "Save All";
            this.buttonSaveAll.UseVisualStyleBackColor = false;
            this.buttonSaveAll.Click += new System.EventHandler(this.buttonSaveAll_Click);
            // 
            // buttonSaveText
            // 
            this.buttonSaveText.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("buttonSaveText.BackgroundImage")));
            this.buttonSaveText.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.buttonSaveText.Cursor = System.Windows.Forms.Cursors.Hand;
            this.buttonSaveText.FlatAppearance.BorderColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonSaveText.FlatAppearance.BorderSize = 0;
            this.buttonSaveText.FlatAppearance.CheckedBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonSaveText.FlatAppearance.MouseDownBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonSaveText.FlatAppearance.MouseOverBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonSaveText.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonSaveText.Font = new System.Drawing.Font("Arial", 27.75F, System.Drawing.FontStyle.Bold);
            this.buttonSaveText.Location = new System.Drawing.Point(123, 853);
            this.buttonSaveText.Name = "buttonSaveText";
            this.buttonSaveText.Size = new System.Drawing.Size(400, 50);
            this.buttonSaveText.TabIndex = 0;
            this.buttonSaveText.TabStop = false;
            this.buttonSaveText.Text = "Save";
            this.buttonSaveText.UseVisualStyleBackColor = true;
            this.buttonSaveText.Click += new System.EventHandler(this.buttonSaveText_Click);
            // 
            // buttonSaveColor
            // 
            this.buttonSaveColor.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("buttonSaveColor.BackgroundImage")));
            this.buttonSaveColor.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.buttonSaveColor.Cursor = System.Windows.Forms.Cursors.Hand;
            this.buttonSaveColor.FlatAppearance.BorderColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonSaveColor.FlatAppearance.BorderSize = 0;
            this.buttonSaveColor.FlatAppearance.CheckedBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonSaveColor.FlatAppearance.MouseDownBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonSaveColor.FlatAppearance.MouseOverBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonSaveColor.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonSaveColor.Font = new System.Drawing.Font("Arial", 27.75F, System.Drawing.FontStyle.Bold);
            this.buttonSaveColor.Location = new System.Drawing.Point(760, 853);
            this.buttonSaveColor.Name = "buttonSaveColor";
            this.buttonSaveColor.Size = new System.Drawing.Size(400, 50);
            this.buttonSaveColor.TabIndex = 0;
            this.buttonSaveColor.TabStop = false;
            this.buttonSaveColor.Text = "Save";
            this.buttonSaveColor.UseVisualStyleBackColor = true;
            this.buttonSaveColor.Click += new System.EventHandler(this.buttonSaveColor_Click);
            // 
            // buttonSaveType
            // 
            this.buttonSaveType.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("buttonSaveType.BackgroundImage")));
            this.buttonSaveType.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.buttonSaveType.Cursor = System.Windows.Forms.Cursors.Hand;
            this.buttonSaveType.FlatAppearance.BorderColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonSaveType.FlatAppearance.BorderSize = 0;
            this.buttonSaveType.FlatAppearance.CheckedBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonSaveType.FlatAppearance.MouseDownBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonSaveType.FlatAppearance.MouseOverBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonSaveType.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonSaveType.Font = new System.Drawing.Font("Arial", 27.75F, System.Drawing.FontStyle.Bold);
            this.buttonSaveType.Location = new System.Drawing.Point(1397, 853);
            this.buttonSaveType.Name = "buttonSaveType";
            this.buttonSaveType.Size = new System.Drawing.Size(400, 50);
            this.buttonSaveType.TabIndex = 0;
            this.buttonSaveType.TabStop = false;
            this.buttonSaveType.Text = "Save";
            this.buttonSaveType.UseVisualStyleBackColor = true;
            this.buttonSaveType.Click += new System.EventHandler(this.buttonSaveType_Click);
            // 
            // colorDialogMain
            // 
            this.colorDialogMain.AnyColor = true;
            this.colorDialogMain.FullOpen = true;
            // 
            // FormMainSettings
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ScrollBar;
            this.ClientSize = new System.Drawing.Size(1920, 1080);
            this.Controls.Add(this.comboBoxType);
            this.Controls.Add(this.listBoxType);
            this.Controls.Add(this.pictureBoxColor);
            this.Controls.Add(this.buttonSaveType);
            this.Controls.Add(this.buttonSaveColor);
            this.Controls.Add(this.buttonSaveText);
            this.Controls.Add(this.buttonColor);
            this.Controls.Add(this.textBoxText);
            this.Controls.Add(this.listBoxColor);
            this.Controls.Add(this.listBoxText);
            this.Controls.Add(this.buttonSaveAll);
            this.Controls.Add(this.buttonExit);
            this.Controls.Add(this.labelTitle);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "FormMainSettings";
            this.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Custom Game Show";
            this.Load += new System.EventHandler(this.FormMainSettings_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxColor)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button buttonExit;
        private System.Windows.Forms.Label labelTitle;
        private System.Windows.Forms.ListBox listBoxText;
        private System.Windows.Forms.TextBox textBoxText;
        private System.Windows.Forms.ListBox listBoxColor;
        private System.Windows.Forms.Button buttonColor;
        private System.Windows.Forms.PictureBox pictureBoxColor;
        private System.Windows.Forms.ListBox listBoxType;
        private System.Windows.Forms.ComboBox comboBoxType;
        private System.Windows.Forms.Button buttonSaveAll;
        private System.Windows.Forms.Button buttonSaveText;
        private System.Windows.Forms.Button buttonSaveColor;
        private System.Windows.Forms.Button buttonSaveType;
        private System.Windows.Forms.ColorDialog colorDialogMain;
    }
}